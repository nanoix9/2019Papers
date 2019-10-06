#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from glob import glob 
import re

def norm_loc(loc):
    loc = loc.lower()
    loc = re.sub(r'\s*//.*$', '', loc)
    loc = loc.split(',')[-1]
    loc = loc.strip()
    # if loc.startswith('us')
    return loc

def norm(k):
    if k in {'canada', 'us'}:
        return 'na'
    elif k in {'belarus', 'finland', 'helsinki', 'hungary', 'lithuania', 'poland', 'uk', 'ukraine'}:
        return 'eu'
    elif k in {'brazil', 'mexico city'}:
        return 'la'
    elif k in {'india'}:
        return 'india'
    elif k in {'malaysia', 'vietnam'}: 
        return 'sea'
    else:
        return k 
        
def sum_stat(stat):
    summ = {}
    for k, v in stat.items():
        sk = norm(k)
        summ.setdefault(sk, 0)
        summ[sk] += v
    return summ

def main():
    stat = {}
    stat['china'] = 5

    def cal_one(fpath):
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line.startswith('- %l:'):        
                    continue
                loc = norm_loc(line.replace('- %l:', '').strip())
                print('\tloc: ' + loc)
                stat.setdefault(loc, 0)
                stat[loc] += 1

    for fpath in glob('devops-agile.log/*.code.md'):
        print('processing ' + fpath)
        cal_one(fpath)

    summ = sum_stat(stat)

    print(', '.join(sorted(stat.keys())))
    print(stat)
    print(summ)
    total = sum(summ.values())
    print(total)
    print({k: float(v) * 100 / total for k, v in summ.items()})

if __name__ == '__main__':
    main()
