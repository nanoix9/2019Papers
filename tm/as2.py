#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from glob import glob
from tqdm import tqdm
import pickle
import pprint
pp = pprint.PrettyPrinter(indent=2)

# from multiprocessing import Pool
import itertools
from collections import namedtuple, Counter, OrderedDict
import re
# from xml.etree import ElementTree
# from xml.etree.ElementTree import ParseError
from bs4 import BeautifulSoup
# from datetime import datetime
import pandas as pd

from spellchecker import SpellChecker
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer

_DEBUG = True
# _DEBUG = False

STOPWORDS = set(stopwords.words("english"))
## Add more stopwords manually
STOPWORDS.update(['i\'m', 'i´m', 'don´t', '\'m', '\'s', '\'re', '\'ve',
    'haha', 'hah', 'wow', 'hehe', 'heh',
    'ah', 'ahh', 'hm', 'hmm', 'urllink', 'ok', 'hey', 'yay', 'yeah'])
print('stop words:', STOPWORDS)

################################################################################
##                        Utility functions                                    #
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

        return [list(map(_helper, doc)) for doc in docs]

def map3d(f, docs):
    with tqdm(total=len2d(docs)) as pbar:
        def _helper(sent):
            pbar.update(1)
            return [f(word) for word in sent]

        return [list(map(_helper, doc)) for doc in docs]
    
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

def filter3d(f, docs):
    ret = []
    with tqdm(total=len2d(docs)) as pbar:
        def _helper_doc(doc):
            for sent in doc:
                pbar.update(1)
                out = [word for word in sent if f(word)]
                if len(out) > 0:
                    yield out
            
        for doc in docs:
            out = list(_helper_doc(doc))
            if len(out) > 0:
                ret.append(out)
    return ret

################################################################################
##              Codes for data reading & transformation                        #
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

    ## save to pickle file for fast loading next time
    if cache_file is not None:
        with open(cache_file, 'wb') as f:
            print('save dataset to pickle file ' + cache_file)
            pickle.dump(dataset, f)

    return dataset

def read_blogs_xml(path):
    print('reading all data files from directory {} ...'.format(path))
    dataset = []

    if _DEBUG:  # use small files for fast debugging
        files = [os.path.join(path, fname) for fname in ['3998465.male.17.indUnk.Gemini.xml',
            '3949642.male.25.indUnk.Leo.xml', '3924311.male.27.HumanResources.Gemini.xml']]
        files = [os.path.join(path, fname) for fname in ['554681.female.45.indUnk.Sagittarius.xml']]
        # files = list(glob(os.path.join(path, '*')))[:3]
        # files = list(glob(os.path.join(path, '*')))[:10]
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
##              Codes for topic mining                         #
################################################################################

punct_re = re.compile(r'([\.!?,:;])(?=[a-zA-Z])')  # add space between a punctuation and a word
## replace two or more consecutive single quotes to a double quote
##   e.g. '' -> "       ''' -> "
quotes_re = re.compile(r'[\']{2,}')  
# escape_re = re.compile(r'\\([\'\"\,\;\:]+)')
def preprocess(text):
    out = punct_re.sub(r'\1 ', text)
    out = quotes_re.sub(r'"', out)
    # out = escape_re.sub(r'\1', out)
    out = remove_invalid(out)
    # if out != text: print('-->', text, '\n   ', out)
    return out

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
    with tqdm(total=sum(len(rec.posts) for rec in dataset)) as pbar:
        for rec in dataset:
            doc = []
            for post in rec.posts:
                # print('-' * 20)
                # if "deceptively" in post.text: print('post:  ', post.text)
                for sent_str in nltk.sent_tokenize(post.text):
                    sent_str = preprocess(sent_str)
                    sent = [w for w in nltk.word_tokenize(sent_str)]
                    # sent = [w.lower() for w in nltk.word_tokenize(sent_str)]
                    doc.append(sent)
                    # if any("deceptively" in w for w in sent): print('tokens:', sent)
                pbar.update(1)
                # print(doc)
            docs.append(doc)
            # print(doc)
            # return(docs)
    
    # print(docs)
    return docs

def calc_vocab(docs):
    '''Calculate the vocabulary (set of distinct words) from a collection 
      of documents.
    '''

    print('calculating the vocabulary...')
    vocab = set()

    def _helper(sent):
        vocab.update(sent)
    
    foreach2d(_helper, docs)
    return sorted(vocab)

def calc_pos_tags(docs):
    print('POS tagging...')
    def _f(sent):
        try:
            return nltk.pos_tag(sent)
        except IndexError:
            print('error sentence: {}'.format(sent))
            raise
    tagged_docs = map2d(_f, docs)
    return tagged_docs

pattern = re.compile(r'([^\.])\1{2,}')
pattern_ellipse = re.compile(r'\.{4,}')
invalid_chars = re.compile(r'[*\^#]')
def remove_invalid(text):
    '''Basic cleaning of words, including:
    
      1. rip off characters repeated more than twice as English words have a max
         of two repeated characters. 
      2. remove characters which are not part of English words
    '''

    text = invalid_chars.sub(' ', text)
    text = pattern.sub(r'\1\1', text)
    text = pattern_ellipse.sub('...', text)
    return text.strip()

def remove_invalid_all(docs):
    print('reduce lengthily repreated characters...')
    return filter3d(lambda w: len(w) > 0, map3d(remove_invalid, docs))

spell = SpellChecker()
# def correct_spelling(sent):
    # misspelled = spell.unknown(sent)
    # print(misspelled)
    # for word in sent:
    #     print(word)
    #     # Get the one `most likely` answer
    #     print(spell.correction(word))

    #     # Get a list of `likely` options
    #     print(spell.candidates(word))
    # sys.exit()
def correct_spelling(word):
    # return word
    if not wordnet.synsets(word) and not word in STOPWORDS:   
        return spell.correction(word)
    else:
        return word

def correct_spelling_all(docs):
    print('running spelling correction...')
    return map3d(correct_spelling, docs)

def remove_stopwords(docs):
    print('removing stopwords...')
    return filter3d(lambda wp: wp[0].lower() not in STOPWORDS, docs)

lemmatizer = WordNetLemmatizer()
porter = PorterStemmer()
lancaster = LancasterStemmer()
def stem_word(word):
    return porter.stem(word)
    # return lemmatizer.lemmatize(word)

def do_stemming(docs):
    print('stemming or lemmatising words...')
    return map3d(lambda wp: (stem_word(wp[0]), wp[1]), docs)

def calc_ne_all(docs):
    print('extracting named entities...')
    ne = []
    def _calc_ne(sent):
        for chunk in nltk.ne_chunk(sent):
            if hasattr(chunk, 'label'):
                ne.append((chunk.label(), ' '.join(c[0] for c in chunk)))
                # print('NE found:', sent, ne[-1], chunk)
    foreach2d(_calc_ne, docs)
    return ne

def get_things(docs, n=5):
    ne_all = calc_ne_all(docs)
    # print(ne_all)
    # things = filter(lambda wp: wp[1] == 'NN', flatten3d(docs))
    tf = nltk.FreqDist(ne_all)
    print(tf.most_common(50))
    things = [w for t, w in ne_all if w.lower() not in STOPWORDS]
    things = [stem_word(w) for w in things]
    tf = nltk.FreqDist(things)
    print(tf.most_common(50))
    return [w for (w, c) in tf.most_common(n)]

# def calc_tfidf(docs):

#TODO: expand beyond sentence boundary?
def get_surroundings(words, docs, n=4, window=2):
    '''expand the topic to be 2 verb/noun before and 2 verb/noun after the topic
    '''

    print('get surrounding {} nouns/verbs for words {}'.format(window, words))

    sur = OrderedDict()
    for w in words:
        sur[w] = Counter() 

    ## POS tags list for searching verbs/nouns 
    target_pos_tags = ('NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBP', 'VBD', 'VBN',
            'VBG', 'VBZ')

    def _helper(sent):
        # print(sent)
        sent_w = [w for w, p in sent]
        for w in words:
            try:
                idx = sent_w.index(w)
            except ValueError:
                continue

            # print('found: {} at {} in {}'.format(w, idx, sent))
            after = 0
            for (wi, pi) in sent[(idx+1):]:
                if pi in target_pos_tags:
                    sur[w][(wi, pi)] += 1
                    after += 1
                    # print('add after: ' + str((wi, pi)))
                if after == window:
                    break

            before = 0
            for (wi, pi) in reversed(sent[:idx]):
                if pi in target_pos_tags:
                    sur[w][(wi, pi)] += 1
                    before += 1
                    # print('add before: ' + str((wi, pi)))
                if before == window:
                    break

    foreach2d(_helper, docs)
    ret = OrderedDict()
    for k, c in sur.items():
        ret[k] = c.most_common(n)
    return ret

#TODO: remove stop words.
def mine_topic_by_freq(dataset):
    # print(dataset)
    # 
    docs = tokenise(dataset)
    vocab = calc_vocab(docs)
    print('Size of vocabulary: {}'.format(len(vocab)))
    print(vocab[:500])

    # docs = remove_invalid_all(docs)
    # vocab = calc_vocab(docs)
    # print('Size of vocabulary: {}'.format(len(vocab)))
    # print(vocab[:500])
    # for v in vocab:
    #     print(v, porter.stem(v), lancaster.stem(v), lemmatizer.lemmatize(v))

    # docs = list2d(correct_spelling_all(docs))
    # vocab = calc_vocab(docs)
    # print('Size of vocabulary: {}'.format(len(vocab)))
    # print(vocab[:500])

    tagged_docs = calc_pos_tags(docs)
    # print(tagged_docs[0][0])
    # print(tagged_docs[0][1])
    # print(tagged_docs[0][2])
    # print(sorted(set(p for w, p in flatten3d(tagged_docs))))

    things = get_things(tagged_docs, n=50)
    print('things: ', things)

    ## Remove stopwords after POS tagging and NER finished
    tagged_docs = remove_stopwords(tagged_docs)
    # print(list2d(tagged_docs)[0])

    tagged_docs = do_stemming(tagged_docs)
    # print('counting word frequencies...')
    # tf = nltk.FreqDist(flatten3d(tagged_docs))
    # print(tf.most_common(50))

    keywords = get_surroundings(things, tagged_docs, n=20, window=2)
    pp.pprint(keywords)


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
