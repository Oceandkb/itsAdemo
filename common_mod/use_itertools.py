#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/30 16:02
@Author : chao
@File   : use_itertools.py
'''

import itertools

# itertools中的无限迭代器

# count方法会创建一个无限迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     # 打印自然数
#     print(n)

# cycle()会将序列无限的重复下去
# cs = itertools.cycle('ABC')
# for i in cs:
#     print(i)

# repeat方法负责吧一个元素无限重复下去
# 但是可以通过传入第二个参数来规定重复次数
rep = itertools.repeat('1', 5)
for r in rep:
    print(r)

# 无限序列只有在for循环时，才会无限次的迭代

# itertools的一些函数：

# 1. 通过takewhile()去截取无限序列中的一部分
natuals = itertools.count(1)
ns = itertools.takewhile(lambda  x: x<= 10, natuals)
print(list(ns))

# 2. chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# 3. groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AABBCCCCCaaACcc', lambda c: c.upper()):
    print(key, list(group))
# lambda函数：lambda arguments: expression

# 练习
def pi(N):
    # 创建一个奇数序列
    # 取序列前N项
    # 添加正负号并用4除
    # 求和
    num = itertools.count(1, 2)
    n_num = list(itertools.takewhile(lambda x: x<=2*N-1, num))
    f_num = []
    for i, value in enumerate(n_num):
        if i % 2 == 0:
            f_num.append(4 / value)
        else:
            f_num.append(4 / -value)
    result = sum(f_num)
    return result


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
