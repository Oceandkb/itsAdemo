#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/12 20:27
@Author : chao
@File   : use_json.py
'''
# 使用json这种标准格式实现信息的传输和存储
import json
d = dict(name='Mc.Flurry', age=1, gender='male')
j = json.dumps(d) # 使用该方法可以返回一个字符串，内容为标准的json格式
print(j)

# dump方法可以直接把一个对象转换为json格式并写入一个file-like Object中
# 将json反序列化，使用loads或者load
json_str = '{"name": "1+1", "age": 1, "gender": "male"}'
d1 = json.loads(json_str)
print(d1)

# 对class进行序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('mc', 1, 88)
# print(json.dumps(s)) # 如果直接使用dumps进行序列化，无法实现
# 通过定一个转换函数，传入dumps的参数中，实现对Student实例的序列化
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
# 也可以通过将类的实例话转化成dict
print(json.dumps(s, default=lambda obj:obj.__dict__))
# 将json反序列化成一个Student类的实例
# loads方法先返回一个dict，然后通过object_hook函数将dict转换成实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"name": "mcflurry", "age": 1, "score": 88}'
cs = json.loads(json_str, object_hook=dict2student)
print(cs)

# practise
# 对中文进行json序列化时，json.dumps提供了一个ensure_ascii参数，观察参数对结果的影响
obj = dict(name = "麦旋风", age = 1)
js1 = json.dumps(obj, ensure_ascii=True)
js2 = json.dumps(obj, ensure_ascii=False)
print('js1:', js1)
print('js2:', js2)
# 当ensure_ascii的参数值为true时，json串中的中文会以ascii码的形式输出

