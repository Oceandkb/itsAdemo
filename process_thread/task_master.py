#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/22 16:39
@Author : chao
@File   : task_master.py
'''
# 学习managers模块如何把多进程任务分配到其他多台机器上
# managers支持把一个服务进程作为调度者，将任务分不到其他多个进程中

# 例子：将一个通过queue通信的多进程任务，从一台机器上分配到两台机器上，实现分布式进程

import multiprocessing
# 分布式进程
import random, time, queue
# BaseManager是multiprocessing中的一个类，用于进程间的资源共享和管理
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support

# 创建发送任务的队列：
task_queue = multiprocessing.Queue()
# 创建接受结果的队列：
result_queue = multiprocessing.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    # 必须要创建一个类继承BaseManager，BaseManager是基类，不能直接用来创建对象
    pass

# 创建获取任务队列和结果队列的函数
def get_task_queue():
    return task_queue
def get_result_queue():
    return result_queue

if __name__ == '__main__':
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象：
    QueueManager.register('get_task_queue', callable = get_task_queue)
    # 两个参数：
    # 1. name：要注册的共享对象的名称，用于在网络上标识共享对象，其他进程通过这个名称获取共享对象的引用
    # 2. callable: 可调用的对象，用于获取共享对象，通常是一个函数或者方法
    QueueManager.register('get_result_queue', callable = get_result_queue)
    # 绑定端口5000，设置验证码'abc'：
    # 创建一个QueueManager类的实例manager
    # 通过传入address参数去绑定服务器ip和端口号，authkey相当于一个验证码（防止其他机器干扰）
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 调用start方法启动QueueManager服务
    manager.start()

    # 获得通过网络访问的Queue对象：
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n) # 向task队列中放东西

    # 从result队列读取结果：
    print('Try get results...')
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('The queue is empty')

    # 关闭：
    manager.shutdown()
    print('master exit.')