#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/25 16:04
@Author : chao
@File   : use_collections.py
'''

from collections import namedtuple
# namedtuple创建自定义的tuple对象，规定了tuple元素格式，且可以通过属性引用tuple元素
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple)) # 验证Point是否为tuple的子类
# namedtuple的作用就是可以定义一类的数据类型，比如定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque 为了实现高效插入和删除操作的双向列表，适用于队列和栈
# 可以高校的向头部插入和删除元素
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y') # 支持appendleft
print(q)
q.popleft() # 支持popoleft，无入参，删除左侧头部第一个元素
print(q)

# defaultdict，当引用dict时key不存在，可以使用defaultdict来避免返回keyerror，而是返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = ['abc']
print(dd['key1'])
print(dd['key2']) # 不存在的的key会返回定义好的defaultdict

# OrderedDict，使用该方法来保持dict的key的顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)]) # 使用Orderdict定义有序dict
print(od)
# OrderdDict是按照插入的key的顺序
# OrderDict可以实现FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capaacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap：把一组dict串起来组成一个逻辑上的dict，本身也是一个dict
# 查找时，会按照顺序在内部的dict依次查找
# 作用情景：
# 当入参可以通过命令行、环境变量和默认参数传入时候，可以用ChainMap实现优先级查找
from collections import ChainMap
import os, argparse

# 构造缺省参数：（缺省参数就是默认参数）
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# 使用字典推导式将命令行参数转换为字典

# 组合成ChainMap：
combined = ChainMap(command_line_args, os.environ, defaults)
# 按照顺序传入参数，然后组成一个有序的dict

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 当命令行输入参数时，优先打印命令行参数

# counter 计数器，类
# 统计字符出现的个数
from collections import Counter
c = Counter() # 创建一个Counter类的对象c
for i in 'programming':
    # 循环迭代一个字符串，计算字符串中每个字母出现的次数
    c[i] = c[i] + 1

print(c)