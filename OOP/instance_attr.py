#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/15 10:45
@Author : chao
@File   : instance_attr.py
'''
# 实例属性和类属性

# 给根据类床架男的实例绑定属性，可以绑定任意属性
# 通过self变量绑定
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
# 通过实例绑定
s.score = 90

# 给类本身绑定属性，可以通过直接在class中定义属性
class Student_1(object):
    name = 'Student_1'

# 定义了类的属性后，但类的所有实例都可以访问到
s1 = Student_1()
print(s1.name) # 如果实例没有name属性，会向上查找类的属性
print(Student_1.name) # 查找类的name属性
s1.name = 'Daming'
print(s1.name) # 实例本身的name属性，优先级比类的name属性高
print(Student_1.name) # 为实例绑定name属性后，不影响类的name属性
del s1.name
print(s1.name) # 删除实例的属性后，访问到的是类的属性

# 所以在为实例和类绑定属性时，千万不要用同名，不然实例的属性就会覆盖掉类的属性
# 且删除实例属性后，访问到的就是类的属性

# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student_p(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student_p.count += 1

if Student_p.count != 0:
    print('测试失败!')
else:
    bart = Student_p('Bart')
    if Student_p.count != 1:
        print('测试失败!')
    else:
        lisa = Student_p('Bart')
        if Student_p.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student_p.count)
            print('测试通过!')