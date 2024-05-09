#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/30 11:13
@Author : chao
@File   : use_struct.py
'''
# python提供了一个struct模块解决bytes和其他二进制数据类型的转换
import struct

s = struct.pack('I', 10240099)
print(s)