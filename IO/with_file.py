#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/23 19:36
@Author : chao
@File   : with_file.py
'''
# 文件读写

# 读文件
f = open('/Users/chao/Desktop/txt.txt', 'r') # open内置函数，传入文件路径和读写方式，r代表只读
print(f.read()) # 通过调用read方法，读取打开文件的内容
f.close() # 关闭文件，使用完成后必须要关闭文件，否则会占用操作系统资源
# 为了保证无论是否读写出错都可以正确的关闭文件，使用try...finally
try:
    f = open('/Users/chao/Desktop/txt.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 为了方便，使用with语句自动调用close
with open('/Users/chao/Desktop/txt.txt', 'r') as f:
    print(f.read())

'''
read()方法会一次性读取文件全部内容
为了防止文件过大，内存溢出，可以反复调用read(size)，每次最多读取size个字节的内容
调用readline()可以每次读取一行的内容
调用readlines()可恶意一次读取所有内容并按行返回list， 通常用于读取配置文件
'''
with open('/Users/chao/Desktop/txt.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

# 通过open返回的有多个read方法的对象，成为file-like Object

# 二进制文件，如图片、视频等，使用'rb'
p = open('/Users/chao/Desktop/pic.JPG', 'rb')
print(p.read())
p.close()

# 读取非utf-8编码的文件，需要传入encoding参数
# 读取GBK文件
# with open('/Users/chao/Desktop', 'r', encoding='gbk') as g:
#     print(g.read())

# 如果文件中有部分非法的编码内容，可以传入errors参数，忽略这些非法编码字符
# with open('/Users/chao/Desktop', 'r', encoding='gbk', errors='ignore') as g:
#     print(g.read())

# 写文件. 'w'标识符
# a代表追加到文件结尾，如果不传入a，则会覆盖原来的内容
with open('/Users/chao/Desktop/txt.txt', 'a', encoding='utf8') as w1:
    w1.write('a brand new cat')

with open('/Users/chao/Desktop/txt.txt','r') as r1:
    print(r1.read())

