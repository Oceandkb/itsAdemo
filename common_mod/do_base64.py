#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/29 15:32
@Author : chao
@File   : do_base64.py
'''

# base64是一种用64个字符表示任意二进制数据的方法
import base64
b = base64.b64encode(b'thisismyworld') #  使用b64encode进行编码
p = base64.b64decode(b'dGhpc2lzbXl3b3JsZA==') # decode解码
# b'str'表示字节
print(b)
print(p)

# base64编码后会出现+和/，但是这种在url中无法被识别
# 所以有一种url safe的base64编码，把编码后的+和/变成-和_
b1 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b11 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print('b1 is %s' % b1) # 输出'abcd++//'
print('b11 is %s' % b11) # 输出'abcd--__'


# 练习
# 请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    # 判断入参的字符串长度是否为4的倍数
    # 是倍数：直接执行decode
    # 不是倍数：根据余数在入参后边加上（4-余数）个=号（字符串）
    # 然后执行decode
    di = len(s) % 4
    if di == 0:
        ds = base64.b64decode(s)
        print('the decode result is %s' % ds)
    else:
        cha = '='
        count = 4 - di
        s = s + cha * count
        ds = base64.b64decode(s)
        print('the decode result is %s' % ds)
    return ds


# safe_base64_decode('YWJjZA')
# safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA==')
print('ok')