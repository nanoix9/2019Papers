#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from glob import glob
from tqdm import tqdm
import pickle
import json
from datetime import date
import pprint
pp = pprint.PrettyPrinter(indent=2)

# from multiprocessing import Pool
import random
import itertools
from collections import namedtuple, Counter, OrderedDict, defaultdict
import heapq
from operator import itemgetter
import re
# from xml.etree import ElementTree
# from xml.etree.ElementTree import ParseError
from bs4 import BeautifulSoup
# from datetime import datetime
import numpy as np

from spellchecker import SpellChecker
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer 
# from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer

NUM_SAMPLES = None
_DEBUG = False
NUM_SAMPLES = 10000
NUM_SAMPLES = 5000
# NUM_SAMPLES = 5

# _DEBUG = True

STOPWORDS = set(stopwords.words("english"))
## Add more stopwords manually
with open('stopwords1.txt') as f:
    STOPWORDS.update(w.strip().lower() for w in f)
STOPWORDS.update(['i\'m', 'dont', '\'t', '\'m', '\'s', '\'re', '\'ve',
    'haha', 'hah', 'wow', 'hehe', 'heh',
    'ah', 'ahh', 'hm', 'hmm', 'urllink', 'ok', 'hey', 'yay', 'yeah'])

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
            # if len(out) > 0:
            ret.append(out)
    return ret

def load_pkl(fpath):
    print('load dataset from cached pickle file ' + fpath)
    with open(fpath, 'rb') as f:
        dataset = pickle.load(f)
    return dataset
   
def save_pkl(obj, fpath):
    with open(fpath, 'wb') as f:
        print('save dataset to pickle file ' + fpath)
        pickle.dump(obj, f)

def save_json(obj, fpath, indent=2):
    with open(fpath, 'w', encoding="utf8") as f:
        print('save dataset to json file ' + fpath)
        json.dump(obj, f, indent=indent)

################################################################################
##              Codes for data reading & transformation                        #
################################################################################

Record = namedtuple('Record', ['meta', 'posts'])
Post = namedtuple('Post', ['date', 'text'])
MetaData = namedtuple('MetaData', ['id', 'gender', 'age', 'category', 'zodiac'])

def parse_meta_data(meta_data_str):
    arr = meta_data_str.lower().strip().split('.')
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
        return load_pkl(cache_file)
 
    dataset = read_blogs_xml(path)

    ## save to pickle file for fast loading next time
    if cache_file is not None:
        save_pkl(dataset, cache_file)

    return dataset

def read_blogs_xml(path):
    print('reading all data files from directory {} ...'.format(path))
    dataset = []

    if _DEBUG:  # use small files for fast debugging
        files = [os.path.join(path, fname) for fname in ['3998465.male.17.indUnk.Gemini.xml',
            '3949642.male.25.indUnk.Leo.xml', '3924311.male.27.HumanResources.Gemini.xml']]
        # files = [os.path.join(path, fname) for fname in ['554681.female.45.indUnk.Sagittarius.xml']]
        # files = list(glob(os.path.join(path, '*')))[:3]
        # files = list(glob(os.path.join(path, '*')))[:10]
        files = random.sample(list(glob(os.path.join(path, '*'))), 100)
        # files = random.sample(list(glob(os.path.join(path, '*'))), 5000)
    elif NUM_SAMPLES is None:
        files = glob(os.path.join(path, '*'))
    else:
        files = random.sample(list(glob(os.path.join(path, '*'))), NUM_SAMPLES)

    for fpath in  tqdm(files):
        # print(fpath)
        fname = os.path.basename(fpath)
        meta_data = parse_meta_data(fname)
        # print(meta_data)
        posts = read_blog_file(fpath)
        rec = Record(meta_data, posts)
        dataset.append(rec)
    return dataset

################################################################################
##              Codes for topic mining                         #
################################################################################

punct_re = re.compile(r'([\.!?,:;])(?=[a-zA-Z])')  # add space between a punctuation and a word
## replace two or more consecutive single quotes to a double quote
##   e.g. '' -> "       ''' -> "
quotes_re = re.compile(r"[\']{2,}")  
# escape_re = re.compile(r'\\([\'\"\,\;\:]+)')
def preprocess(text):
    # print(text)
    out = punct_re.sub(r'\1 ', text)
    # print(out)
    out = quotes_re.sub(r'"', out)
    # print(out)
    out = out.replace('´', '\'')
    # print(out)
    # out = escape_re.sub(r'\1', out)
    out = remove_invalid(out)
    # print(out)
    # if out != text: print('-->', text, '\n   ', out)
    return out

leading_quote_re = re.compile(r'[\'\.~=*&^%#!|\-]+([a-zA-Z].*)')
def clean_word(word):
    if word in ("'ve", "'re", "'s", "'t", "'ll", "'m", "'d", "'", "''"):
        return word
    # if len(word) == 0 or not word.startswith("-"): return word
    # print(word, len(word))
    word = leading_quote_re.sub(r'\1', word)
    # print(word)
    return word.strip()

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
                    # print(sent_str)
                    sent = [clean_word(w) for w in nltk.word_tokenize(sent_str)]
                    sent = [w for w in sent if w != '']
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

    # print(text)
    text = invalid_chars.sub(' ', text)
    # print(text)
    text = pattern.sub(r'\1\1', text)
    # print(text)
    text = pattern_ellipse.sub('...', text)
    # print(text)
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
    return porter.stem(lemmatizer.lemmatize(word))
    # return porter.stem(word)
    # return lemmatizer.lemmatize(word)

def do_stemming(docs):
    print('stemming or lemmatising words...')
    return map3d(lambda wp: (stem_word(wp[0]), wp[1]), docs)

def calc_ne_all(docs):
    print('extracting named entities...')
    def _calc_ne(sent):
        ne = []
        for chunk in nltk.ne_chunk(sent):
            if hasattr(chunk, 'label'):
                ne.append((' '.join(c[0] for c in chunk), chunk.label()))
                # print('NE found:', sent, ne[-1], chunk)
        return ne
    return map2d(_calc_ne, docs)

# def get_things(ne_all):
#     # print(ne_all)
#     # things = filter(lambda wp: wp[1] == 'NN', flatten3d(docs))
#     tf = nltk.FreqDist(flatten3d(ne_all))
#     print(tf.most_common(50))
#     things = [w for w, t in flatten3d(ne_all) if w.lower() not in STOPWORDS]
#     # things = [stem_word(w) for w in things]
#     things = set(things)
#     return things
#     # tf = nltk.FreqDist(things)
#     # print(tf.most_common(50))
#     # return [w for (w, c) in tf.most_common(n)]

def calc_df(docs):
    df = defaultdict(lambda: 0)
    # print(docs)
    for doc in docs:
        for w in set(doc):
            df[w] += 1
    # print('df', df)
    return df

def calc_tfidf(docs):
    '''The original TF-IDF is a document-wise score. This function will
    calculate the average TF-IDF on whole dataset as an overall scoring.
    '''
    tf_idf = defaultdict(lambda: 0)
    df = calc_df(docs)
    num_docs = len(docs)
    # print('num docs', num_docs)
    for doc in docs:
        counter = Counter(doc)
        num_words = len(doc)
        # print('---------------------------')
        # print(doc)
        # print('num words', num_words)
        for token in set(doc):
            tf = counter[token] / num_words
            df_i = df[token]
            idf = np.log(num_docs / df_i)
            tf_idf[token] += tf * idf
            # print(token, tf, idf, tf * idf)
    
    for token in tf_idf:
        # tf_idf[token] /= num_docs
        tf_idf[token] /= df[token]

    return tf_idf

def get_top_topics(named_entities, n=5, method='tf'):
    print('calculating most popular topics by ' + method + '...')
    if method == 'tf':
        ranks = nltk.FreqDist(w for w, t in flatten3d(named_entities))
        print(ranks.most_common(50))
        ranks = dict(ranks)
    elif method == 'tfidf':
        ranks = calc_tfidf([[w for w, t in flatten2d(doc)] for doc in named_entities])
        # print(ranks)
    ranks = [(k, v) for k, v in ranks.items()]
    print('n largest:', heapq.nlargest(200, ranks, key=itemgetter(1)))
    topics = heapq.nlargest(n, ranks, key=itemgetter(1))
    print('topics: ', topics)
    # return [w for (w, c) in topics]
    return topics

def get_surroundings(words, docs, n=4):
    '''expand the topic to be 2 verb/noun before and 2 verb/noun after the topic
    '''

    print('get surrounding 2 nouns/verbs for words {}'.format(words))

    sur = {}
    for w, c in words:
        sur[w] = Counter() 

    ## POS tags list for searching verbs/nouns 
    # target_pos_tags = ('NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBP', 'VBD', 'VBN',
            # 'VBG', 'VBZ')

    def _helper(sent):
        # print(sent)
        sent_w = [w for w, p in sent]
        for w, c in words:
            try:
                idx = sent_w.index(w)
            except ValueError:
                continue

            # print('found: {} at {} in {}'.format(w, idx, sent))
            after = 0
            vicinity = [sent[i] for i in [idx-2, idx-1, idx+1, idx+2]
                    if i >= 0 and i < len(sent)]
            for (wi, pi) in vicinity:
                if pi.startswith('N') or pi.startswith('V'):
                    # sur[w][(wi, pi)] += 1
                    sur[w][wi] += 1
                    # print('add: ' + str((wi, pi)))

    foreach2d(_helper, docs)
    ret = []
    for w, c in words:
        ret.append({'topic': w, 'score': c, 'keywords': sur[w].most_common(n)})
    return ret

def calc_intermediate_data(dataset):
    # print(dataset)
    # 
    docs = tokenise(dataset)
    vocab = calc_vocab(docs)
    print('Size of vocabulary: {}'.format(len(vocab)))
    print(vocab[1:2000:2])
    print(vocab[1:100000:100])

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
    docs = vocab = None

    named_entities = calc_ne_all(tagged_docs)

    ## Remove stopwords after POS tagging and NER finished
    tagged_docs = remove_stopwords(tagged_docs)
    named_entities = remove_stopwords(named_entities)
    # print(list2d(tagged_docs)[0])

    tagged_docs = do_stemming(tagged_docs)
    named_entities = do_stemming(named_entities)
    # print('counting word frequencies...')
    # tf = nltk.FreqDist(flatten3d(tagged_docs))
    # print(tf.most_common(50))
    return tagged_docs, named_entities

def mine_topics(dataset, intermediate_data, group='all'):
    print('-' * 80)
    print('mining most popular topics for group ' + group)
    print('-' * 80)
    tagged_docs, named_entities = intermediate_data

    if group != 'all':
        if group == 'male' or group == 'female':
            idx = [i for i, rec in enumerate(dataset) if rec.meta.gender == group]
        elif group == '<=20':
            idx = [i for i, rec in enumerate(dataset) if rec.meta.age <= 20]
        elif group == '>20':
            idx = [i for i, rec in enumerate(dataset) if rec.meta.age > 20]
        else:
            raise NotImplementedError()
        tagged_docs = [tagged_docs[i] for i in idx]
        named_entities = [named_entities[i] for i in idx]
        
    print('selected docs: {}, {}'.format(len(tagged_docs), len(named_entities)))
    # things = get_things(named_entities)
    # things = set(w for w, t in named_entities)
    # print('things: ', random.sample(things, 200))

    ret = {}
    num_keywords = 200
    print('-------------- result from TFIDF ------------------')
    topics = get_top_topics(named_entities, n=50, method='tfidf')
    # print('most popular topics by TFIDF: {}'.format(topics))
    keywords = get_surroundings(topics, tagged_docs, n=num_keywords)
    # pp.pprint(keywords)
    ret['tfidf'] = keywords

    print('-------------- result from TF ------------------')
    topics = get_top_topics(named_entities, n=50, method='tf')
    # print('most popular topics by TF: {}'.format(topics))
    keywords = get_surroundings(topics, tagged_docs, n=num_keywords)
    # pp.pprint(keywords)
    ret['tf'] = keywords
    return ret

def main_intermediate():
    if not _DEBUG and NUM_SAMPLES is None:
        dataset = read_blogs('blogs')
    else:
        # read_blogs('blogs', force=True, cache_file='blogs-10.pkl')
        # dataset = read_blogs('.', cache_file='blogs-10.pkl')
        dataset = read_blogs('blogs', cache_file=None)

    intermediate_data = calc_intermediate_data(dataset)
    save_pkl(intermediate_data, 'intermediate_data.pkl')
    return dataset, intermediate_data

def main_mine_topics(dataset=None, intermediate_data=None):
    if dataset is None:
        dataset = load_pkl('blogs.pkl')
    if intermediate_data is None:
        intermediate_data = load_pkl('intermediate_data.pkl')

    topics = {}
    topics['male'] = mine_topics(dataset, intermediate_data, group='male')
    topics['female'] = mine_topics(dataset, intermediate_data, group='female')
    topics['less_or_20'] = mine_topics(dataset, intermediate_data, group='<=20')
    topics['over_20'] = mine_topics(dataset, intermediate_data, group='>20')
    topics['all'] = mine_topics(dataset, intermediate_data, group='all')
    if _DEBUG:
        suffix = 'debug'
    else:
        suffix = date.today().strftime('%Y%m%d')
        if NUM_SAMPLES > 0:
            suffix += '-' + str(NUM_SAMPLES)

    save_json(topics, 'topics-{}.json'.format(suffix))

def main():
    # print('stop words:', sorted(STOPWORDS))
    if len(sys.argv) <= 1:
        phases = [1, 2]
    else:
        phases = [int(i) for i in sys.argv[1].split(',')]

    dataset = intermediate_data = None
    for ph in phases:
        if ph == 1:
            dataset, intermediate_data = main_intermediate()
        elif ph == 2:
            main_mine_topics(dataset, intermediate_data)

if __name__ == '__main__':
    main()
