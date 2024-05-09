#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/9 10:18
@Author : chao
@File   : use_chardet.py
'''
import chardet

print(chardet.detect(b'Hello, world!')) # b代表一个字节字符串
# result: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# confidence标识检测的概率，1.0代表100%

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

