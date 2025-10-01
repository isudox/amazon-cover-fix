#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from cover import Cover
from filelist import Filelist

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix cover image of Amazon Kindle books')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('mode', help='Cover quality')
    args = parser.parse_args()
    print('filepath:{}'.format(args.input))

    filelist = Filelist(args.input)
    asins = filelist.list_asin()
    cover = Cover(asins, args.mode)
    cover.download()
