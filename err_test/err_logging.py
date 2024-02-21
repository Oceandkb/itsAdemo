#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 17:16
@Author : chao
@File   : err_logging.py
'''

# python内置的logging模块可以很容易的记录错误信息
import logging

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
# 尽管会报错，但是打印完错误信息后，程序会继续执行，并正常退出
print('END')

# 通过配置，logging还可以把错误记录到日志文件里，方便排查