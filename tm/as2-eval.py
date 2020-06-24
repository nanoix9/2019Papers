#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import numpy as np
import pandas as pd
from as2 import load_pkl, Record, MetaData, Post
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


def color_black(word, *args, **kwargs):
    return '#000000'

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # return 'hsl(0, 0%, {:d}%)'.format(np.random.randint(10, 60))
    return 'hsl(0, 0%, {:d}%)'.format((MAX_FONT_SIZE - font_size) // (MAX_FONT_SIZE * 1))

def eval_topics(fpath, method='tf', top_k=2, num_words_in_topic=20):
    with open(fpath, encoding='utf8') as f:
        result = json.load(f)

    for group, topics2 in result.items():
        # print(group)
        topics = topics2[method]
        for i, topic in enumerate(topics[:top_k]):
            topic_name = topic['topic']
            words = {}
            words.update(tuple(kw) for kw in topic['keywords'][:num_words_in_topic+1])
            if method == 'tf':
                words[topic_name] = topic['score']
            else:
                words[topic_name] = topic['keywords'][0][1] * 2  # fake frequency for display

            print('topic: ', topic_name, 'number of keywords:', len(topic['keywords']))
            wc = WordCloud(background_color="white", 
                    max_font_size=80, 
                    max_words=num_words_in_topic+1,
                    color_func=grey_color_func)
            wc.generate_from_frequencies(words)

            # show
            plt.clf()
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")
            # plt.show()
            plt.title(topic_name, y=-0.25, fontsize=20)
            plt.gcf().tight_layout()
            fig_path = 'img/{}-{}-{}.png'.format(group, method, i+1, topic['topic'])
            print('drawing ' + fig_path)
            plt.savefig(fig_path)

def main():
    cmd = sys.argv[1]
    if cmd == 'show':
        show_summary(load_pkl('blogs.pkl'))
        # show_summary(load_pkl('blogs-10.pkl'))
    elif cmd == 'eval':
        fpath = sys.argv[2]
        eval_topics(fpath, top_k=2)
        eval_topics(fpath, top_k=2, method='tfidf')

if __name__ == '__main__':
    main()
