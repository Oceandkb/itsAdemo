#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/15 15:09
@Author : chao
@File   : use_slots.py
'''
# 使用__slots__
class Student(object):
    pass

s = Student()
s.name = 'Michael' # 给实例绑定属性
print(s.name)


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定方法
s.set_age(25)
print(s.age)

# 对单个实例绑定方法是无法应用到其他实例上的
# 可以通过给class绑定方法，去给所有实例都绑定上
def set_score(self, score):
    self.score = score

Student.set_score = set_score # 为类绑定方法后，所有实例均可用

s.set_score(100)
print(s.score)

# 按照常理应该是把方法定义到class中，但是动态语言允许在程序运行过程中添加功能

# 如果想要限制实例的属性，可以使用__slots__
class Student_1(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s1 = Student_1()
s1.name = 'Bob'
s1.age = 19
# s1.score = 89 # 绑定限制外的属性，程序报错
print(s1.name, s1.age)
# print(s1.score)

# ⚠️，slot限制的属性只对当前类的实例有用，对子类的实例无效
class Pri_student(Student_1):
    pass

p = Pri_student()
# 子类没有使用slot，父类的slot也不生效
p.score = 89
print(p.score)

class Sen_student(Student_1):
    __slots__ = ('gender')

# 如果子类中定义了slot，那么该子类的实例允许绑定的属性为父类的slot和子类的slot
se = Sen_student()
se.score = 88
print(se.score) # 输出报错，因为score属性不在父类也不在子类中
# print(se.gender)