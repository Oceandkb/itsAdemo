#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/2/21 17:50
@Author : chao
@File   : do_stringio.py
'''

# 数据读写不一定是文件，也可以在内存中读写
# StringIO是在内存读写str

# 创建StringIO
from io import StringIO
f = StringIO()
# 写入
f.write('hello')
print(f.getvalue()) # 使用getvalue方法输出str

# 读取StringIO
f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())