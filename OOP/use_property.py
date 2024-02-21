#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/15 18:04
@Author : chao
@File   : use_property.py
'''
# 使用property
# 直接给实例绑定属性，但是属性暴露在外边，可以随便设置
# 前边通过在class中设置set_score去控制传入参数值，用get_score获取属性
# 为了方便，可以用property装饰器

class Student(object):
    @property # 负责把一个方法变成属性调用
    def score(self):
        '''
        在不用property装饰的情况下，获取score定义的是get方法
        而使用property装饰，就可以把这个方法变成属性去直接访问（第44行）
        :return:
        '''
        return self._score # 注意属性名称不要和方法名称重名，否则在调用时会造成无限递归
    '''
    detail reason:
    这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，
    于是又转换为方法调用，造成无限递归，最终导致栈溢出报错RecursionError。
    '''

    @score.setter # 使用property装饰后，会自动创建另一个装饰器setter，负责把set方法变成为属性赋值（43行）
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

# 还可以创建只读属性，不定义setter方法即可
    @property
    def age(self):
        return 18

s = Student()
# s.score = 101 # 抛出异常
s.score = 90
print(s.score)
print(s.age)

# 练习
# 请利用@property给一个Screen对象加上width和height属性
# 以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, w_value):
        if not isinstance(w_value, int):
            raise ValueError('width must be integer')
        if w_value < 0:
            raise ValueError('width must be positive')
        self._width = w_value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, h_value):
        if not isinstance(h_value, int):
            raise ValueError('height must be integer')
        if h_value < 0:
            raise ValueError('height must be positive')
        self._height = h_value

    @property
    def resolution(self):
        self._resolution = self.width * self.height
        return self._resolution

 # test
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


