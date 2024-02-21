#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 15:26
@Author : chao
@File   : use_metaclass.py
'''
# 使用元类
# type()函数可以获取对象的类型，也可以创建新的类
class Hello(object):
    pass

h = Hello()
print(type(h)) # h是一个实例，类型是class Hello
print(type(Hello)) # Hello是一个class，类型是type
# 使用type创建一个新的类
def fn(self, name='world'):
    '''
    先定义一个输出函数
    :param self:
    :param name:
    :return:
    '''
    print('Hello, %s.' % name)

# type()入参：
# 1. 类名
# 2. 元祖(包含继承的父类，注意元祖的书写方式)
# 3. 一个字典，包含新类的属性和方法
Hello1 = type('Hello1', (object,), dict(hello = fn))
h1 = Hello1()
h1.hello()

# 元类 metaclass
# metaclass是用来创建类的（类似通过类创建实例）：先定义metaclass，然后创建类，最后创建实例
