#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/13 20:15
@Author : chao
@File   : use_fork.py
'''

import os


print('Process (%s) start...' % os.getpid()) # getpid获取当前进程的id

pid = os.fork()
# unix/linux提供了fork的系统调用（windows无）
# 调用一次fork，返回两次
# 系统把当前进程复制一个子进程，然后分别在父进程和子进程中返回
# 父进程返回子进程id，子进程返回0
# 子进程调用getppid方法获取父进程id
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 调用一次fork，第一次是父进程，返回子进程的id，输出else语句
# 第二次是子进程，返回的是0，输出if下的语句
