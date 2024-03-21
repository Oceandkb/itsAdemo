#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/20 20:19
@Author : chao
@File   : do_queue.py
'''
# 进程间的通信
# 使用multiprocess模块中提供的Queue进行通信
from multiprocessing import Queue, Process
import os, time, random

# 写数据
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        # Queue的put方法将数据放入队列中，并将其打印
        q.put(value)
        print('Put %s to queue...' % value)
        time.sleep(random.random())

# 读数据
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        # Queue的get方法从队列中获取数据，并将其打印
        value = q.get(True)
        print('Get %s from queue' % value)

if __name__ == '__main__':
    # 父进程创建queue，并传给各子进程
    # 实例化一个Queue
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是死循环，所以要强制终止
    pr.terminate()

