#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/19 20:02
@Author : chao
@File   : do_subprocess.py
'''

# 子进程并不是自身，而是一个外部进程
# 使用subprocess模块可以启动一个子进程，控制输入和输出
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# subprocess模块首先推荐run方法
'''
subprocess.run(args, *, stdin=None, input=None, stdout=None,
 stderr=None, capture_output=False, shell=False, cwd=None, timeout=None,
  check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
'''
# args: 要执行的命令，必须是字符串，字符串参数列表
# shell: True代表通过操作系统的shell执行指定命令
# stdout: 子进程的输出，值可以是subprocess.PIPE，将命令的标准输出重定向到一个管道，以便代码后续处理（我认为是
# stderr: 子进程的错误
# timeout: 设置命令超时时间

subprocess.run(["ls", "-l", "/dev/null"])
def runcmd(command):
    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding="utf-8", timeout=1)
    if ret.returncode == 0:
        print("success:", ret)
    else:
        print("error:", ret)

runcmd(["ls", "-l"]) # 序列参数
runcmd("exit 1") # 字符串参数

# Popen方法，是subprocess的核心，子进程的创建和管理都靠它处理
'''
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, 
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)
'''

# p = subprocess.Popen('ls -l', shell=True)
# p = subprocess.Popen(['ls', '-cl'])
import time

def cmd(command):
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, encoding="utf-8")
    subp.wait(2) # 等待子进程终止
    if subp.poll() == 0:
        # poll()检查进程是否终止，如果终止返回returncode，否则返回none
        print(subp.communicate()[1])
        # communicate(input, timeout) 和子进程交互，发送和读取数据
    else:
        print("失败")


cmd("python -version")
cmd("exit 1")