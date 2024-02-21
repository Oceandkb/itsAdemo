#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 11:27
@Author : chao
@File   : use_enum.py
'''
# 使用枚举类
from enum import Enum
# 定义一个月份的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec'))
# 通过Month.Jan来引用一个常量，或者枚举它所有的成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value属性是自动赋给成员的int常量，默认从1开始计数

# 更精确地控制枚举类，可以从Enum派生出自定义类
from enum import Enum, unique

@unique # unique装饰器可以帮助检查没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被定义为0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问枚举类型
day1 = Weekday.Mon # 使用成员名称引用枚举常量
print(day1)
print(day1.value) # 根据value值获得枚举常量
print(day1 == Weekday.Mon)
print(Weekday(1))
for name, member in Weekday.__members__.items():
    print(name, '=>', member, member.value)


# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender(0)) # 或者使用Gender.Male
if bart.gender == Gender.Male:
    print('pass')
else:
    print('false')

'''
枚举类(Enum)是一种数据类型
Enum可以把一组相关常量定义在一个class中，class不可变，而且成员可以直接比较
'''