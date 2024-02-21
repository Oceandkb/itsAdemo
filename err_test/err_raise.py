#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 17:22
@Author : chao
@File   : err_raise.py
'''
# 抛出错误
# 错误是class，所以捕获一个错误就是class的一个实例
# 自己定义的函数也可以抛出错误
class FooError(ValueError):
    pass

def foo(s):
   n = int(s)
   if n==0:
       raise FooError('invalid value: %s' % s)
   return  10 / n

foo('0')