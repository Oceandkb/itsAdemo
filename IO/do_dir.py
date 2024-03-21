#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/2/21 19:57
@Author : chao
@File   : do_dir.py
'''
# 操作文件和目录
import os
print(os.name) # 输出电脑操作系统类型
# posix，说明系统是linux、unix或mac os x
# nt，代表是windows

# 获取详细的操作系统信息（windows系统不提供uname方法
print(os.uname())

# 查看环境变量
print(os.environ)
# 获取某个环境变量的值(PATH是想要查看的环境变量的值
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建新的目录
# 先把新目录的完整路径表示出来
os.path.join('/Users/chao/Desktop/Chao/Code/itsAdemo/', 'testdir')
# 然后创建
os.mkdir('/Users/chao/Desktop/Chao/Code/itsAdemo/testdir')
# 删除目录
os.rmdir('/Users/chao/Desktop/Chao/Code/itsAdemo/testdir')

# 使用os.path.join()合并两个路径，为了适应不同操作系统的分隔符
# 同理，使用os.path.split()拆分路径，后一部分是拆分前路径的最后一级
# os.path.splitext可以直接拆分出这个文件的拓展名
a = os.path.splitext('/Users/chao/Desktop/Chao/Code/itsAdemo/IO/do_dir.py')
print(a)

'''
注：这些拆分和合并并不要求路径真实存在，只是对字符串进行合并和拆分
'''

# 重命名文件
# os.rename('/Users/chao/Desktop/Chao/Code/itsAdemo/IO/test.py', 'test1.py')
# 删除文件
# os.remove('test1.py')

# 复制文件，使用shutil模块中的copyfile
import shutil
shutil.copyfile('/Users/chao/Desktop/Chao/Code/itsAdemo/IO/do_dir.py',
                '/IO/dir_prac.py')

# 输出当前目录下的所有目录
dict = '/Users/chao/Desktop/Chao/Code/itsAdemo'
d = [x for x in os.listdir(dict) if os.path.isdir(os.path.join(dict ,x))]
print(d)

# 输出所有py文件
p = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(p)











import os
# 练习
# 1. 利用os模块编写一个能实现dir -l输出的程序



# 2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''
查看当前目录和子目录
过滤包含自定义字符串的文件
'''
fd = os.path.abspath('.') # 当前目录
# kd = os.listdir(fd) # 获取当前目录下的所有子目录和文件
# # listdir返回的是一个列表
# # 遍历这个列表
# for item in kd:
#     kd_path = os.path.join(fd, item)
#     if os.path.isdir(kd_path):
#         # 判断是否为子目录
#         print(kd_path)

search_str = 'dir'
[x for x in fd and os.listdir(fd) if os.path.isfile(x) and search_str in x]


