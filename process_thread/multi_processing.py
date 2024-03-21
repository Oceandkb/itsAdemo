#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/13 20:33
@Author : chao
@File   : multi_processing.py
'''

# python本身提供了编写多进程的模块：multiprocessing
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    # Process类代表一个进程对象，创建一个Process类的实例
    print('Child process will start.')
    p.start() # 启动p这个实例
    p.join() # join方法可以等待子进程结束后再继续往下运行（先去执行子进程，然后再执行剩余代码
    print('Child process end.')