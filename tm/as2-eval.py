#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import numpy as np
import pandas as pd
from as2 import load_pkl, Record, MetaData, Post
import matplotlib.pyplot as plt


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

def eval_topics(fpath):
    with open(fpath, encoding='utf8') as f:
        result = json.load(f)

    for group, topics in result:
        print(group)

def main():
    cmd = sys.argv[1]
    if cmd == 'show':
        show_summary(load_pkl('blogs.pkl'))
        # show_summary(load_pkl('blogs-10.pkl'))
    elif cmd == 'eval':
        fpath = sys.argv[2]
        eval_topics(fpath)

if __name__ == '__main__':
    main()
