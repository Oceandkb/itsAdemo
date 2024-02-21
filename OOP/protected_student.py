#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/11 17:46
@Author : chao
@File   : protected_student.py
'''

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 98)
# bart.__score # 外部访问私有变量时找不到了，AttributeError: 'Student' object has no attribute '__score'

# 为了能够让外部获取私有属性，或者修改，可以在类中添加方法
class Student(object):
    def __init__(self, name, socre):
        self.__name = name
        self.__score = socre

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        '''
        创建方法修改属性，可以在方法中定义想要的校验，防止无效参数传入
        :param score:
        :return:
        '''
        if score <= 100 and score >= 0:
            self.__score = score
        else:
            raise ValueError('bad score')
            # print('输入成绩不合法，成绩修改失败')


lisa = Student('Lisa', 86)
print(lisa.get_name())
print(lisa.get_score())
# lisa.set_score(109) # ValueError: bad score 修改成绩失败

'''
⚠️__xxx__, 这种类型的代表特殊变量，可以直接访问
_name, 这种一个下划线的变量，虽然不是private， 但是意思是请把我看作private，不要随便访问
__name虽然为private，但是也可以通过lisa._Student_name去访问（不过不要这么做，不同的python版本是不同的
'''

# 练习: 把gender对外隐藏，使用get和set代替
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender == 'female' and 'male':
            self.__gender = gender
            return '性别修改成功'
        else:
            raise ValueError('bad gender')

amy = Student('Amy', 'male')
if amy.get_gender() != 'male':
    print('测试失败!')
else:
    amy.set_gender('female')
    if amy.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
