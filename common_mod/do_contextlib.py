#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/7 16:16
@Author : chao
@File   : do_contextlib.py
'''

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
# 声明一个contextmanager装饰器，接受一个generator
def creat_query(name):
    print('Begin')
    q = Query(name)
    yield q
    # 通过yield语句把with...as var把变量输出出去，然后with语句就可以正常工作
    print('End')

# with语句
# 当需要在代码块执行前后有一些特定操作时，使用with
# with 上下文表达式 [as 变量]： （as 变量是用于将上下文管理器的返回赋值给一个变量）
#    代码块

with creat_query('Bob') as q:
    q.query()

# 当在执行某段代码前后想要执行特定的代码，也可以用contextmanager
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print("hello")
    print('world')

# 上边代码的执行顺序：
# with语句先执行yield之前的语句
# 然后执行with语句内部所有的语句
# 最后执行yield后边的语句

# 所以contextmanager的作用是简化的实现上下文管理

# closing
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

@contextmanager
# 定义
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
