#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

amazon_cover_url = 'https://m.media-amazon.com/images/P/'


class Cover:
    def __init__(self, asin_ids: dict, mode: str):
        self.asin_ids = asin_ids
        self.mode = mode
        self.amazon_cover_url = 'https://m.media-amazon.com/images/P/'
        self.thumbnail_filename = 'thumbnail_{}_EBOK_portrait.jpg'
        self.thumbnail_filepath1 = 'thumbnails1/'
        self.thumbnail_filepath2 = 'thumbnails2/'

    def download(self):
        cnt = 0
        for asin_id, filename in self.asin_ids.items():
            if self.mode == '1':
                thumbnail_suffix = '.jpg'
                thumbnail_filepath = self.thumbnail_filepath1
            else:
                thumbnail_suffix = '.01.MAIN._SCRM_.jpg'
                thumbnail_filepath = self.thumbnail_filepath2
            thumb_img_url = self.amazon_cover_url + asin_id + thumbnail_suffix
            data = requests.get(thumb_img_url).content
            f = open(thumbnail_filepath + self.thumbnail_filename.format(asin_id), 'wb')
            f.write(data)
            f.close()
            cnt += 1
        print('Downloaded {} thumbnails'.format(cnt))
