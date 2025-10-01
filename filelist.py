#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
from typing import Any

sample = 'B008QM7U98'


class Filelist:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def list_asin(self) -> dict[Any, Any]:
        ret = {}
        filenames = [f for f in listdir(self.filepath) if isfile(join(self.filepath, f))]
        for f in filenames:
            b0_index = f.find("_B0")
            if b0_index == -1:
                continue
            # 计算结束索引，确保不会超出字符串长度
            end_index = b0_index + 11
            if end_index > len(f):
                end_index = len(f)
            asin_id = f[b0_index + 1:end_index]
            ret[asin_id] = f
        print(ret)
        return ret
