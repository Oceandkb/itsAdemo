#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/16 16:14
@Author : chao
@File   : multi_inherit.py
'''
# 多重继承
# 使用动物分类做例子，如果按照哺乳类、鸟类，会飞和不会飞分类去进行继承会很麻烦
# 使用多重继承就可以解决这个问题
class Animal(object):
    pass
# 大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# 各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

# 给动物加上走地和飞的功能
# 先定义好这两个类
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying')
# 回到定义的动物类，如果需要这两个功能的，只需要多继承一个类即可

class Dog1(Mammal, Runnable):
    pass
class Bat1(Mammal, Flyable):
    pass

# 通过多重继承，子类就可以继承多个父类的功能
# 当设计类的继承时，通常都是一条主线继承下来的，比如Dog继承Mammal，Mammal继承Animal
# 当想要给Dog增加额外的功能，可以通过多重继承，比如Dog继承一个Runnable类
# 这种方法叫做MixIn，在设计时优先使用多重继承，而不是使用复杂的继承


'''
python也有很多使用了MixIn
如TCPServer和UDPServer两类服务，而要同时服务多个用户就必须使用多进程或多进程模型
这两种模型由ForkingMixIn和ThreadingMixIn提供

'''
class MyTCPServer(TCPServer, ForkingMixIn):
    pass