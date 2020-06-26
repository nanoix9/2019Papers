#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from glob import glob
from tqdm import tqdm
from collections import Counter, defaultdict
import numpy as np
from numpy.linalg import norm
import pandas as pd
from as2 import load_pkl, save_pkl, Record, MetaData, Post, \
    stem_word, flatten3d, foreach3d, lemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

MAX_FONT_SIZE = 80

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
    df['char_count'] = [sum(len(p.text) for p in d.posts) for d in dataset]

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

    plt.rcParams.update({'font.size': 20})
    # df.hist()
    df['gender'].value_counts().plot(kind='bar')
    plt.xticks(rotation=0)
    # plt.show()
    plt.gcf().tight_layout()
    plt.savefig('img/show-gender.png')

    plt.rcParams.update({'font.size': 10})
    plt.clf()
    df['category'].value_counts().plot(kind='bar')
    # plt.xticks(rotation=45)
    # plt.yscale('log')
    plt.gcf().tight_layout()
    plt.savefig('img/show-category.png')

    plt.rcParams.update({'font.size': 18})
    plt.clf()
    df['zodiac'].value_counts().plot(kind='bar')
    plt.xticks(rotation=90)
    plt.gcf().tight_layout()
    plt.savefig('img/show-zodiac.png')

    plt.rcParams.update({'font.size': 20})
    plt.clf()
    age = df['age']
    # bins = np.linspace(age.min(), age.max(), 20)
    df['age'].hist(bins=20)
    # plt.xticks(bins)
    plt.gcf().tight_layout()
    plt.savefig('img/show-age.png')

    plt.clf()
    cnt = df['blog_count']
    logbins = np.logspace(np.log10(cnt.min()),np.log10(cnt.max()), 20)
    cnt.hist(bins=logbins)
    plt.xscale('log')
    plt.gcf().tight_layout()
    plt.savefig('img/show-blog-count.png')

    plt.clf()
    cnt = df['char_count']
    logbins = np.logspace(np.log10(cnt.min()),np.log10(cnt.max()), 20)
    cnt.hist(bins=logbins)
    plt.xscale('log')
    plt.gcf().tight_layout()
    plt.savefig('img/show-char-count.png')

    plt.clf()
    df['gender_age'] = [g + '\n' + ('<=20' if a <= 20 else '>20') \
            for (g, a) in zip(df['gender'], df['age'])]
    # bins = np.linspace(age.min(), age.max(), 20)
    df['gender_age'].value_counts()[[2, 3, 1, 0]].plot(kind='bar')
    # plt.xticks(bins)
    plt.xticks(rotation=0)
    plt.gcf().tight_layout()
    plt.savefig('img/show-gender-age.png')

def calc_stem_map():
    '''Map word stem back to the most representative word so we can display valid
    English words in the word cloud, and also for calculating the coherence score
    '''

    print('building map from stem to words ...')
    docs = load_pkl('tokenised_docs.pkl')

    stem2word = defaultdict(lambda *_, **__: Counter())
    def _helper(w):
        s = stem_word(w)
        stem2word[s][lemmatizer.lemmatize(w.lower())] += 1
        # print(stem2word)

    print('calculating map...')
    foreach3d(_helper, docs)

    out = {}
    for k, cnt in stem2word.items():
        out[k] = cnt.most_common(10)
    # print(out)
    save_pkl(out, 'stem2word.pkl')
    return out

## Colour functions for word cloud
def color_black(word, *args, **kwargs):
    return '#000000'

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # return 'hsl(0, 0%, {:d}%)'.format(np.random.randint(10, 60))
    return 'hsl(0, 0%, {:d}%)'.format((MAX_FONT_SIZE - font_size) // (MAX_FONT_SIZE * 1))

STEM2WORD = None
def eval_topics(fpath, method='tf', top_k=2, num_words_in_topic=10):
    '''Evaluate topics by:
      1. plotting the word cloud
      2. calculating the diagnostic and coherence metrics
    '''

    with open(fpath, encoding='utf8') as f:
        result = json.load(f)

    global STEM2WORD
    if STEM2WORD is None:
        STEM2WORD = load_pkl('stem2word.pkl')

    def _2w(w):
        if w in STEM2WORD:
            return STEM2WORD[w][0][0]
        else:
            return w

    topics_formatted = {}
    for group, topics2 in result.items():
        # print(group)
        topics = topics2[method]
        topics_formatted[group] = []
        for i, topic in enumerate(topics[:top_k]):
            topic_name = _2w(topic['topic'])
            words = {}
            words.update((_2w(kw[0]), kw[1]) for kw in topic['keywords'][:(num_words_in_topic-1)])
            if method == 'tf':
                words[topic_name] = topic['score']
            else:
                try:
                    words[topic_name] = topic['keywords'][0][1] * 2  # fake frequency for display
                except IndexError:
                    words[topic_name] = 1
            topics_formatted[group].append((topic_name, words))

    print(topics_formatted)
    plot_topics(topics_formatted, method=method)
    return calc_coherence_all(topics_formatted, method=method)

LSA = None
def load_lsa():
    global LSA
    if LSA is None:
        print('loading LSA model...')
        try:
            LSA = load_pkl('lsa.pkl')
        except:
            print('failed')
            print('loading LSA model...')
            with open('semilar/LSA-MODELS/LSA-MODEL-TASA-LEMMATIZED-DIM300/voc.txt') as f:
                vocab = [x.strip() for x in f]
            # print(vocab[:10])
            print('vocab size:', len(vocab))

            with open('semilar/LSA-MODELS/LSA-MODEL-TASA-LEMMATIZED-DIM300/lsaModel.txt') as f:
                vec = [np.array([float(x) for x in line.split()]) for line in f]
            print('vector size:', len(vec), len(vec[0]))
            # print(vec[0])
            LSA = {w: v for w, v in zip(vocab, vec)}
            save_pkl(LSA, 'lsa.pkl')
    return LSA
    
WIKI_PMI = None
def load_wiki_pmi():
    global WIKI_PMI
    if WIKI_PMI is None:
        print('loading wiki PMI model...')
        try:
            WIKI_PMI = load_pkl('wiki-pmi.pkl')
        except:
            print('load from original files...')
            WIKI_PMI = {}
            for fname in tqdm(glob('semilar/wiki-pmi/*')):
                with open(fname) as f:
                    next(f)
                    next(f)
                    next(f)
                    next(f)
                    for line in f:
                        a, b, s = line.strip().split()
                        s = float(s)
                        WIKI_PMI[(a, b)] = s
                        # break
                    # print(WIKI_PMI)

            save_pkl(WIKI_PMI, 'wiki-pmi.pkl')

    return WIKI_PMI

GLOVE = None
def load_glove(ndim=100):
    global GLOVE
    if GLOVE is None:
        print('loading glove embeddings...')
        try:
            GLOVE = load_pkl('glove{}.pkl'.format(ndim))
        except:
            print('failed')
            GLOVE = {}
            fname = 'embeddings/glove.6B.{}d.txt'.format(ndim)
            print('load from file', fname)
            with open(fname) as f:
                for line in f:
                    arr = line.strip().split()
                    GLOVE[arr[0].strip()] = np.array([float(f) for f in arr[1:]])
                    # break
                # print(GLOVE)

            save_pkl(GLOVE, 'glove{}.pkl'.format(ndim))

    return GLOVE

def cosine_similarity(a, b):
    return np.dot(a, b)/(norm(a)*norm(b))

def lsa_score(wi, wj):
    lsa = load_lsa()
    vi = lsa[wi]
    vj = lsa[wj]
    return cosine_similarity(vi, vj)

def pmi_score(wi, wj):
    pmi = load_wiki_pmi()
    p = (wi, wj)
    if p in pmi:
        return pmi[p]
    else:
        return pmi[wj, wi]

def glove_score(wi, wj):
    lsa = load_glove()
    vi = lsa[wi]
    vj = lsa[wj]
    return cosine_similarity(vi, vj)

def calc_coherence(words, f):
    n = 0
    score = 0.0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            try:
                score += f(words[i], words[j])
            except KeyError:
                print('warning: cannot find pairwise association: {} {}' \
                        .format(words[i], words[j]))
                continue
            n += 1
            # print(i, j, words[i], words[j], score, n)
    return score / n

def calc_word_length(words):
    return sum(len(w) for w in words) / len(words)

WORD_COUNT = None
def calc_topic_size(words):
    global WORD_COUNT
    if WORD_COUNT is None:
        docs, _ = load_pkl('intermediate_data.pkl')
        WORD_COUNT = Counter(w for w, t in flatten3d(docs))
    return sum(WORD_COUNT[w] for w in words)

def calc_coherence_all(topics_all, method):
    metrics = []
    for group, topics in topics_all.items():
        # print(group)
        for i, (topic_name, words_freq) in enumerate(topics):
            if len(words_freq) <= 1:
                continue
            words = sorted(words_freq.keys())
            print('topic:', topic_name, words)
            lsa = calc_coherence(words, lsa_score)
            print('lsa score', lsa)
            # pmi = calc_coherence(words, pmi_score)
            # print('pmi score', pmi)
            we_glove = calc_coherence(words, glove_score)
            print('we glove score', we_glove)
            wl = calc_word_length(words)
            print('avg word length', wl)
            ts = calc_topic_size(words)
            print('avg topic size', ts)
            metrics.append((group, i, topic_name, words, lsa, we_glove, wl, ts))
    return metrics

def print_metrics_as_table(metrics, fpath):
    '''Plot metrics as \LaTeX table
    '''

    with open(fpath, 'w') as f:
        for group, i, topic, keywords, lsa, we_glove, wl, ts in metrics:
            if i > 0:
                group = ' '
            elif group == 'less_or_20':
                group = '20 or younger'
            elif group == 'over_20':
                group = 'over 20'
            elif group == 'all':
                group = 'everyone'
            f.write(f'{group} & {topic} & {ts//1000:,}k & {wl:.1f} & {lsa:.3f} & {we_glove:.3f} \\\\\n')
            if i == 1:  # two topics for each group
                f.write('\\hline\n')
            else:
                f.write('\\cline{2-6}\n')

def plot_topics(topics_json, method):
    '''Plot word cloud for the keywords in each topic
    '''

    for group, topics in topics_json.items():
        # print(group)
        for i, (topic_name, words) in enumerate(topics):
            print('topic: ', topic_name, 'number of keywords:', len(words))
            wc = WordCloud(background_color="white", 
                    max_font_size=80, 
                    max_words=len(words)+1,
                    color_func=grey_color_func)
            wc.generate_from_frequencies(words)

            # show
            plt.clf()
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")
            # plt.show()
            # plt.title(topic_name, y=-0.25, fontsize=20, fontname='Times New Roman')
            plt.title(topic_name, y=-0.25, fontsize=20, fontname='Georgia')
            plt.gcf().tight_layout()
            fig_path = 'img/{}-{}-{}.png'.format(group, method, i+1, topic_name)
            print('drawing ' + fig_path)
            plt.savefig(fig_path)

def main():
    cmd = sys.argv[1]
    if cmd == 'show':
        show_summary(load_pkl('blogs.pkl'))
        # show_summary(load_pkl('blogs-10.pkl'))
    elif cmd == 'eval':
        fpath = sys.argv[2]
        metrics_tf = eval_topics(fpath, top_k=2, method='tf')
        metrics_tfidf = eval_topics(fpath, top_k=2, method='tfidf')
        print('tf metrics', metrics_tf)
        print_metrics_as_table(metrics_tf, 'metrics-tf.tex')
        print('tfidf metrics', metrics_tfidf)
        print_metrics_as_table(metrics_tfidf, 'metrics-tfidf.tex')
    elif cmd == 'stem2word':
        calc_stem_map()

if __name__ == '__main__':
    main()
