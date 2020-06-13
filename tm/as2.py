#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from glob import glob
from tqdm import tqdm
import pickle

import itertools
from collections import namedtuple, Counter
import pandas as pd
# from xml.etree import ElementTree
# from xml.etree.ElementTree import ParseError
from bs4 import BeautifulSoup
# from datetime import datetime

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

_DEBUG = True

sw = stopwords.words("english")

# tqdm = lambda x, *args, **kwds: x

################################################################################
#                        Utility functions                                     #
################################################################################

def len2d(iter2d):
    return sum(len(d) for d in iter2d)

def list2d(iter2d):
    return [[x for x in inner] for inner in iter2d]

def flatten2d(list2d):
    return itertools.chain.from_iterable(list2d)

def flatten3d(list3d):
    return itertools.chain.from_iterable(flatten2d(list3d))

def mapbar(f, seq, desc):
    for e in tqdm(seq, desc):
        yield f(e)

def map2d(f, docs):
    with tqdm(total=len2d(docs)) as pbar:
        def _helper(sent):
            pbar.update(1)
            return f(sent)

        for doc in docs:
            yield map(_helper, doc)

def map3d(f, docs):
    with tqdm(total=len2d(docs)) as pbar:
        def _helper(sent):
            pbar.update(1)
            return [f(word) for word in sent]

        for doc in docs:
            yield map(_helper, doc)
    
def foreach3d(f, docs):
    with tqdm(total=len2d(docs)) as pbar:
        for doc in docs:
            for sent in doc:
                for word in sent:
                    f(word)
                pbar.update(1)

def foreach2d(f, docs):
    with tqdm(total=len2d(docs)) as pbar:
        for doc in docs:
            for sent in doc:
                f(sent)
                pbar.update(1)

################################################################################
#              Codes for data reading & transformation                         #
################################################################################

Record = namedtuple('Record', ['meta', 'posts'])
Post = namedtuple('Post', ['date', 'text'])
MetaData = namedtuple('MetaData', ['id', 'gender', 'age', 'category', 'zodiac'])

def parse_meta_data(meta_data_str):
    arr = meta_data_str.strip().split('.')
    return MetaData(arr[0], arr[1], int(arr[2]), arr[3], arr[4])

# _parser = ElementTree.XMLParser(encoding="utf-8")
def read_blog_file(fpath):
    try:
        # tree = ElementTree.parse(fpath, parser=_parser)
        with open(fpath, encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), "xml")
        blog = soup.Blog
    except ParseError:
        print('Error: invalid xml file {}'.format(fpath))
        raise
        return []

    posts = []
    state = 'date'
    for c in blog.find_all(recursive=False):
        # print(c)
        # print(c.text)
        # check the <date> and <post> tags appear alternately
        if c.name != state:
            print('Warning: inconsistent format in file {}'.format(fpath))
        if state == 'date':
            try:
                date_str = c.text.strip()
                # date_str = date_str.replace('janvier', 'january') \
                #     .replace('mars', 'march') \
                #     .replace('avril', 'april') \
                #     .replace('mai', 'may') \
                #     .replace('juin', 'june') \
                #     .replace('juillet', 'july')
                # date = pd.to_datetime(date_str, format='%d,%B,%Y')
                date = date_str
            except ValueError:
                print('Warning: invalid date {} in file {}' \
                        .format(c.text, fpath))
                # date = datetime.fromtimestamp(0)
            state = 'post'
        else:
            text = c.text.strip()
            state = 'date'
            posts.append(Post(date, text))
        # print(c, c.text)
    posts.sort(key=lambda p: p.date)
    # print(posts)
    # print(pd.DataFrame(posts))
    # sys.exit()
    return posts
    
def read_blogs(path, force=False, cache_file='blogs.pkl'):
    if not force and cache_file is not None and os.path.exists(cache_file):
        print('load dataset from cached pickle file ' + cache_file)
        with open(cache_file, 'rb') as f:
            dataset = pickle.load(f)
        return dataset
    
    dataset = read_blogs_xml(path)

    # save to pickle file for fast loading next time
    if cache_file is not None:
        with open(cache_file, 'wb') as f:
            print('save dataset to pickle file ' + cache_file)
            pickle.dump(dataset, f)

    return dataset

def read_blogs_xml(path):
    print('reading all data files from directory {} ...'.format(path))
    dataset = []

    if _DEBUG: 
        files = [os.path.join(path, fname) for fname in ['3998465.male.17.indUnk.Gemini.xml',
            '3949642.male.25.indUnk.Leo.xml', '3924311.male.27.HumanResources.Gemini.xml']]
        # for fpath in list(glob(os.path.join(path, '*')))[:3]:
    else:
        files = glob(os.path.join(path, '*'))
    for fpath in  tqdm(files):
        # print(fpath)
        fname = os.path.basename(fpath)
        meta_data = parse_meta_data(fname)
        # print(meta_data)
        posts = read_blog_file(fpath)
        rec = Record(meta_data, posts)
        dataset.append(rec)
    return dataset

def show_summary(dataset):
    '''This function describes the summary of dataset or human inspection.
    It's not necessary for the mining process.

    Parameters
    --------------
    dataset : list of Record
        The blog dataset 
    '''

    df = pd.DataFrame([d.meta for d in dataset])
    df['blog_count'] = [len(d.posts) for d in dataset]
    # print(df)
    print(df.describe(include='all'))
    print('{} possible values for "gender": {}'.format(
            len(df.gender.unique()), ', '.join(sorted(df.gender.unique()))))
    # print('{} possible values for "{}": {}'.format(
    #         len(df.age.unique()), ', '.join(sorted(df.age.unique()))))
    print('{} possible values for category: {}'.format(
            len(df.category.unique()), ', '.join(sorted(df.category.unique()))))
    print('{} possible values for zodiac: {}'.format(
            len(df.zodiac.unique()), ', '.join(sorted(df.zodiac.unique()))))

################################################################################
#              Codes for topic mining                         #
################################################################################

def tokenise(dataset):
    '''
    consider all the blogs from one person as a document

    Returns
    ---------
    docs: list of list of list
        a list of documents, each of which is a list of sentences,
        each of which is a list of words.
    '''

    print('tokenising the text dataset...')
    docs = []
    vocab = set()
    with tqdm(total=sum(len(rec.posts) for rec in dataset)) as pbar:
        for rec in dataset:
            doc = []
            for post in rec.posts:
                # print(post)
                for sent_str in nltk.sent_tokenize(post.text):
                    sent = [w.lower() for w in nltk.word_tokenize(sent_str)]
                    doc.append(sent)
                    vocab.update(sent)
                pbar.update(1)
                # print(doc)
            docs.append(doc)
            # print(doc)
            # return(docs)
    return sorted(vocab), docs

def get_things(docs, n=5):
    things = filter(lambda wp: wp[1] == 'NN', flatten3d(docs))
    tf = nltk.FreqDist(things)
    # print(tf.most_common(50))
    return tf.most_common(n)

# def calc_tfidf(docs):

#TODO: expand beyond sentence boundary?
def get_surroundings(words, docs, n=2):
    '''expand the topic to be 2 verb/noun before and 2 verb/noun after the topic
    '''

    print('get surrounding {} nouns/verbs for words {}'.format(n, words))

    sur = {w: Counter() for w in words}

    target_pos_tags = ('NN', 'NNS', 'VB', 'VBP', 'VBD', 'VBN')

    def _helper(sent):
        # print(sent)
        for w in words:
            try:
                idx = sent.index(w)
            except ValueError:
                continue

            print('found: {} at {} in {}'.format(w, idx, sent))
            after = 0
            for (wi, pi) in sent[(idx+1):]:
                if pi in target_pos_tags:
                    sur[w][(wi, pi)] += 1
                    after += 1
                    print('add after: ' + str((wi, pi)))
                if after == n:
                    break

            before = 0
            for (wi, pi) in reversed(sent[:idx]):
                if pi in target_pos_tags:
                    sur[w][(wi, pi)] += 1
                    before += 1
                    print('add before: ' + str((wi, pi)))
                if before == n:
                    break

    foreach2d(_helper, docs)
    return sur

#TODO: remove stop words.
def mine_topic_by_freq(dataset):
    vocab, docs = tokenise(dataset)
    print('Size of vocabulary: {}'.format(len(vocab)))
    print(vocab[:100])

    print('POS tagging...')
    tagged_docs = list2d(map2d(lambda s: nltk.pos_tag(s), docs))
    # print(tagged_docs[0][0])
    # print(tagged_docs[0][1])
    # print(tagged_docs[0][2])
    # print(sorted(set(p for w, p in flatten3d(tagged_docs))))

    things = get_things(tagged_docs)
    print('things: ', things)

    # print('counting word frequencies...')
    # tf = nltk.FreqDist(flatten3d(tagged_docs))
    # print(tf.most_common(50))

    thing_words = [(w, pos) for ((w, pos), c) in things]
    keywords = get_surroundings(thing_words, tagged_docs, n=2)
    print(keywords)


def main():
    if _DEBUG:
        # read_blogs('blogs', force=True, cache_file='blogs-10.pkl')
        # dataset = read_blogs('.', cache_file='blogs-10.pkl')
        dataset = read_blogs('blogs', cache_file=None)
    else:
        dataset = read_blogs('blogs')

    mine_topic_by_freq(dataset)
    return

if __name__ == '__main__':
    main()
