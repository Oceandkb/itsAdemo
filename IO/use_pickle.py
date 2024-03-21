#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/3/11 20:15
@Author : chao
@File   : use_pickle.py
'''

# 序列化：把变量从内存中变成可存储或传输的过程称之为序列化（pickling
# 把序列化的对象重新存储到内存中，称之为反序列化（unpickling
# 使用pickle模块实现序列化

import pickle
d = dict(name='McFlurry', age = 1, gender = 'male')
print(pickle.dumps(d))

# pickle.dumps方法把任意对象序列化成一个bytes，然后就可以把这个bytes写入文件
# pickle.dump方法可以直接把对象徐立华后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 把一个对象从磁盘读取到内存中
f = open('dump.txt', 'rb')
d = pickle.load(f) # 将一个file-like的对象反序列化
f.close()
print(d)