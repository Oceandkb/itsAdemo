#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/12 17:11
@Author : chao
@File   : attr.py
'''
# 获得一个对象的所有属性和方法，可以使用dir，返回一个包含字符串的list
print(dir('ABC'))

# 如果自己写的类也使用__len__方法，就需要自己写一个
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

# 配合getattr() setattr()以及hasattr()操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
# 获取对象的属性
print(hasattr(obj, 'x')) # 对象obj是否有属性x
print(hasattr(obj, 'y'))
setattr(obj, 'y', 10) # 为对象obj设置一个属性'y'
print(hasattr(obj, 'y'))
print(getattr(obj, 'y')) # 获取对象obj的属性y的值
print(getattr(obj, 'z', 404)) # 如果获取一个不存在的属性，传入参数404，则返回404

# 获取对象的方法
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
# 使用getattr方法将对象的方法指向变量fn
fn = getattr(obj, 'power')
print(fn()) # 调用fn()和obj.power()是一样的效果


'''
举个例子
'''
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
'''
如果在不了解fp对象的情况下，想要对fp进行图像读取的操作
使用hasattr判断fp是否有read方法，如果有再去执行读取操作
'''

