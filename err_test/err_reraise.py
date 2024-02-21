#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 17:30
@Author : chao
@File   : err_reraise.py
'''
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('invalid')
        raise # raise不传入参数，则抛出原样的异常
bar()

# 即使在bar函数调用过程中捕获了错误，也可以使用raise继续向上抛，找到根源