#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/11 15:45
@Author : chao
@File   : student.py
'''

class Student(object):
    # 类名通常大写，object代表这个类的是从哪个类继承的，object类是所有类最终都会继承的类
    pass

# 通过类创建实例
bart = Student() # 实例名=类名+()
print(bart, '\n', Student) # 变量bart指向的是一Student类的一个实例对象，at后为内存地址 <__main__.Student object at 0x1046a6ca0>

# 给实例绑定属性
bart.name = 'Bart Simpson'
print(bart.name)

# 在类中通过_init_方法，定义必有属性，在创建实例时作为参数传入，绑定到实例上
class Student(object):
    def __init__(self, name, score):
        '''
        __init__方法的第一个参数永远是self，表示实例本身
        :param name:
        :param score:
        '''
        self.name = name # self代表实例本身，所以通过self.name，将name属性绑定到实例上
        self.score = score

# ⚠️一旦class有了init方法，在创建实例时就不能传入空的参数，需要传入和init方法对应的参数（self除外）

bart = Student('Bart Simpson', 100)
print('%s: %s' % (bart.name, bart.score))

# 类中的方法和普通方法有一点不同，就是第一个参数永远是self，但是调用时不需要传入，其他和普通方法无差别

# 数据封装
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        '''
        类内定义的函数，称为类的方法，用来封装数据，与数据绑定
        :return:
        '''
        print('%s: %s' % (self.name, self.score))

# 调用类的方法，只需要在类的实例上直接调用
lisa = Student('Lisa Simpson', 98)
lisa.print_score()

# 将数据和逻辑都封装到类中，好处就是调用容易，不需要了解内部实现的细节
# 另外，封装可以给类增加新的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s, %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

luke = Student('Luke Dumpy', 59)
print(luke.name, luke.get_grade())