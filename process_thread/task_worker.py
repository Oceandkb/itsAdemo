#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/22 16:40
@Author : chao
@File   : task_worker.py
'''

# 该文件编写的是master将进程任务分配到的地方，worker
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager：
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
    QueueManager.register('get_task_queue') # 会通过这个名称参数去找master中对应的引用
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器：
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    # 端口和验证码注意保持与task_master.py设置的完全一致
    # 创建一个实例，用去接受任务
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    # 使用connect方法从网络连接：
    m.connect()
    # 获取Queue对象
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 从task队列取任务，并把结果写入result队列：
    for i in range(10):
        try:
            n = task.get(timeout=1) # 从任务队列中取元素
            print('run task %d * %d' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r) # 经过结算后放入结果队列，最后的结果会在master程序输出
        except queue.Empty:
            print('task queue is empty.')
    # 处理结束
    print('worker exit.')