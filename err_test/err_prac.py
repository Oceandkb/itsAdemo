#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 17:36
@Author : chao
@File   : err_prac.py
'''
# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce
import logging

def str2num(s):
    # return int(s)
    # return float(s) # 第一种解决方式
    # 第二种
    try:
        return int(s)
    except ValueError as e:
        logging.exception(e)
        return (float(s))

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()