#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/2/21 18:10
@Author : chao
@File   : do_bytesio.py
'''

# 操作二进制数据，就要使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) # 写入的并不是string，而是通过encode编码的bytes

print(f.getvalue())