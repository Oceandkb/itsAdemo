#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/16 16:42
@Author : chao
@File   : special_class.py
'''
# 定制类
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael')) # 打印出的是Student的实例：<__main__.Student object at 0x10540aca0>
# 通过定义__str()__方法，返回一个好看的字符串
class Student1(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
s = Student1('Bob')
print(s)
# 如果一个类想要被用于for循环，就必须实现一个__iter__()，该方法返回迭代对象
# 使用斐波那契数列为例
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 实例的初始属性a,b
    def __iter__(self):
        return self # 实例本身就是迭代对象，所以返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        # 判断推出循环的条件
        if self.a > 100000:
            raise StopIteration
        return self.a

for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然可以像list一样去循环，但是没办法真的像list一样取值
# 使用__getitem__去获取迭代对象的元素
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, b + a
        return a
# 通过索引位置输出元素
f = Fib1()
print('斐波那契数列的第十位是：%s' % f[10])

# list可以使用切片，但是Fib1不行，是因为__getitem__没有对入参进行校验（int, slice）
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# 输出切片
f2 = Fib2()
print(f2[0:5])

# __getattr__
# 当调用类的方法或者属性不存在时，就会报错
# 通过定义__getattr__方法，动态返回一个属性
class Student2(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student2()
print(s.name)
# 当实例中没有查找的属性或方法时，就会去getattr中查询
print(s.score)
print(s.age())
# ⚠️只有在没有查到属性的情况下才会调用__getattr__
# print(s.abc) # 任意调用返回None，因为__getattr__默认返回就是None
# 若只要求class相应特定的几个属性，其余抛出异常，可以加上一句(87行)

# 利用__getattr__，可以针对完全动态的情况做调用
# 模拟链式调用的方式来构建路径（没太懂为什么使用__getattr__）
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        '''

        :param path: 接受实例中不存的的属性
        :return: 构建新的Chain实例，将现有路径和新路径组合
        '''
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        '''
        用来更改打印出的内容，如果不定义__str__方法，打印出来的是<__main__.Chain object at 0x11f5445b0>
        :return:
        '''
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list) # 链式调用
'''
理解一下这句代码：
Chain()创建了一个实例
Chain().status访问实例的status属性，但是实例没有这个属性，所以调用__getattr__
__getattr__接受status为参数，创建新的Chain实例，这个实例接受已有的self._path/path作为参数，即/status
创建的新的实例的_path属性值为/status
Chain().status.user继续访问了上一步结果的user属性，发现还是没有，所以调用__getattr__方法
接下来就和上边一样了
'''
# __call()__，调用实例本身
class Student3(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s3 = Student3('daming')
s3() # 直接调用实例，不传入参数
# 使用callable函数判断一个变量是对象还是函数(是否可以被调用)
print(callable(s3))
print(callable([1, 3, 4]))