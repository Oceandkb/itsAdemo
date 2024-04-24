#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/22 15:36
@Author : chao
@File   : use_threadlocal.py
'''
# 多线程的一个难点就是线程之间的变量使用
# 使用全局变量的话需要加锁
# 使用局部变量，每个线程执行的函数都要传递
# ThreadLocal提供了一个全局变量，但是对每个线程都可以单独的提供一个独立的数据副本
import threading

# 创建全局的ThreadLocal对象：
local_school = threading.local()
# 每一个线程都可以访问ThreadLocal对象的属性，该例子中是studen属性
# ThreadLocal对象是全局变量，但是不同的线程访问的属性是局部变量，互不干扰



def process_student():
    # 获取当前线程关联的student：
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student：
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal常用的地方是为每一个线程绑定一个数据库链接、http请求、拥护身份信息等
# ThreadLocal解决了同一个参数在各个函数之间相互传递的问题
