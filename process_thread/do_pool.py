#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/15 16:55
@Author : chao
@File   : do_pool.py
'''

# 使用进程池的方式启动大量的子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    '''
    定义一个耗时的方法
    :param name:
    :return:
    '''
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time() # 记录开始时间
    time.sleep(random.random() * 3) # 利用sleep方法来模拟任务耗时时间
    end = time.time() # 记录结束时间
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid()) # 打印父进程id
    # 通过实例化Pool的方式创建一个进程池
    p = Pool(4) # 在实例化Pool这个类时，4这个参数可以规定最大同时执行的进程数
    # Pool的默认大小是CPU的核数
    # 采用循环的方式，使用apply_async方法向线程池提交任务
    for i in range(5):
        p.apply_async(long_time_task, args=(i,)) # 每个任务都调用long_time_task方法
        '''
        注意：这里疑问为什么不能按照long_time_task(i)这种方式写
        询问chatgpt后，得到答案：
        apply_async这种方法的第一个入参要求是一个可调用的对象，而不能是函数值
        使用args=(i,)，将i作为元组的一部分传递给apply_async方法
        result = pool.apply_async(func, args=(), kwds={}, callback=None, error_callback=None)
        参数说明：
        func：要执行的函数或方法。
        args：一个元组，包含传递给函数的位置参数（可选）。
        kwds：一个字典，包含传递给函数的关键字参数（可选）。
        callback：一个可调用对象，用于在任务完成时回调（可选）。
        error_callback：一个可调用对象，用于在发生错误时回调（可选）。
        '''
    print('Waiting for all subprocesses done...')
    p.close() # 关闭进程池
    p.join() # 等待所有子进程执行完毕后，执行后面的代码
    print('All subprocesses done.')