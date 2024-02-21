#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 17:12
@Author : chao
@File   : err.py
'''
# 调用栈
# 当错误没有被except捕获时，就会一直向上抛，直到python捕获，打印一个错误信息，退出程序

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main() # 没有写try...except，会由python解释器抛出异常
