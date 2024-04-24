#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/12 14:56
@Author : chao
@File   : multi_threading.py
'''
# 多线程
# _thread: 低级模块，
# threading：高级模块，对_threading进行了封装，常用模块

import time, threading

# 每个进程都默认有一个线程，称为主线程，启动的新的线程为子线程
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        # current_thread()函数永远返回当前线程的实例
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)

# 创建一个Thread实例，入参是线程所要执行的函数，以及线程名称
t = threading.Thread(target=loop, name='LoopThread')
t.start() # 开始执行
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 该部分代码创建了一个新的线程，在这个线程中执行loop函数


