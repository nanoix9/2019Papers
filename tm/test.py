#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import as2
from collections import Counter

def main():
    docs, ne = as2.load_pkl('intermediate_data.pkl')
    ne = Counter((w, t) for w, t in as2.flatten3d(ne) if w in ('lol', 'fuck', 'Im', 'choru'))
    print(ne.most_common(20))
    return

if __name__ == '__main__':
    main()
