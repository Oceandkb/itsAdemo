#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/12 15:23
@Author : chao
@File   : do_lock.py
'''
import threading

# 多进程中，同一个变量是拷贝存在于每个进程的，所以互不影响
# 多线程中，同一个变量是共享的，所以任何一个线程对变量的改变都会对其他线程产生影响

# 为了防止这种情况，要确保在一个线程修改balance时，别的线程一定不能改
# 使用Lock对线程上锁

balance = 0
lock = threading.Lock() # threading模块中的Lock方法，创建一个锁的实例

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        # 首先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 执行完成后要释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# 当多个线程都执行lock.require时，只有一个线程可以获取锁，其余只能等待锁被释放后执行
# 一定要释放锁
# 使用try...finally确保锁会被释放

# 锁的好处是可以保证一个线程完成的执行
# 坏处是会阻碍并发执行，效率低
# 不同的锁被不同的线程获取时，可能会造成死锁，最终导致程序挂起

