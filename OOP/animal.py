#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/12 10:14
@Author : chao
@File   : animal.py
'''

# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

# 有了Animal类，在定义Dog和Cat类时，就可以直接继承Animal
class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Dog和Cat是Animal的子类。子类通过继承，可以获得父类的全部功能
# 比如Dog和Cat都自动获得了run方法
dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 子类和父类有相同的方法名称时，子类方法覆盖父类的方法，称为多态
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        '''
        子类和父类的同名方法，父类的被覆盖重写
        :return:
        '''
        print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 进一步了解多态，在编写一个函数
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal()) # 传入Animal的一个实例
run_twice(Dog()) # 传入Dog的实例
run_twice(Cat()) # 传入Cat的实例

# 新定义一个Animal的子类
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

# 再去给run_twice传入Tortoise的实例
run_twice(Tortoise())

'''
多态的好处：
当需要传入Dog、Cat或者Tortoise时，只需要接受Animal类型即可
因为这些都是Animal的类型，然后按照Animal类型操作
'''
