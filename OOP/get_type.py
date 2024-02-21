#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/12 16:30
@Author : chao
@File   : get_type.py
'''
# 使用type()

class Animal(object):
    def __init__(self):
        pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()
# 判断对象的类型
print(type(123))
print(type('str'))
print(type(abs)) # 输出函数的类型
print(type(a)) # 输出类的实例的类型

# 使用type判断对象是否为函数
import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)

# 使用isinstance
d = Dog()
h = Husky()
print(isinstance(d, Dog))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Husky))
# 基本类型也可以使用isinstance判断
print(isinstance(123, int))
print(isinstance('str', str))