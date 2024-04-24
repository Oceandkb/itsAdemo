#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/24 11:07
@Author : chao
@File   : regex.py
'''

# 正则表达式
# 用来匹配字符串的工具
# 用描述性的语言来给字符串定义一个规则，符合该规则就认为是匹配的，否则就不合法


# re模块，包含所有正则表达式的功能
import re
m = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
# 使用re模块的match方法去匹配正则表达式和字符串，匹配成功返回一个match对象，否则返回none
# r可以不用考虑转义问题，比如'\-'和r'-'是一样的
if m:
    print('match successfully')
else:
    print('fail')

test = 'qwe-1'
if re.match(r'^\w{3}-[0-9a-z]', test):
    print(1)
else:
    print(0)

# 切分字符串
# 使用split方法切分字符串
# 普通的切分代码
print('a b   c'.split(' ')) # 无法识别连续的空格
# 使用正则表达式
print(re.split(r'\s+', 'a  b   c')) # 无论多少空格都可以分割
print(re.split(r'[\s\,\;]+', 'a,b,c;;;   d'))

# 分组
# 正则表达式可以提取子串的强大功能，用()表示的就是要提取的分组
# 在正则表达式中定义了组后，就可以使用group()的方式提取输出
m1 = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print(m1.group(0)) # group(0)代表完整的字符串
print(m1.group(1)) # group(1)代表第一个子串，依次类推
print(m1.group(2))

t = '19:05:30'
m2 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):'
              r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):'
              r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# 识别合法时间
print(m2.groups()) # 输出所有子串


# 贪婪匹配
# 正则表达式默认是贪婪匹配
m3 = re.match(r'^(\d+)(0*)$', '12300000')
print(m3.groups())
# \d+会把数字全部匹配，导致0*就是空的字符串
m4 = re.match(r'^(\d+?)(0*)$', '102300000')
print(m4.groups())
# 在正则匹配条件后加?，就可以非贪婪匹配

# 编译
# 在使用match匹配时，会有两个步骤：1. 编译正则表达式；2. 用编译后的正则表达式去匹配
# 如果一个正则表达式要多次使用，可以先编译正则表达式，然后直接去匹配
# 使用compile编译
re_tele = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
m5 = re_tele.match('010-12345').groups()
print(m5)


# 练习
# 1. 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

def is_valid_email(addr):
    re_email = re.compile(r'^[a-z.]+@[a-z]*.[a-z]{3}$')
    m6 = re_email.match(addr)
    if m6:
        print(1)
    else:
        print(0)

is_valid_email('someone@gmail.com')
is_valid_email('bill.gates@microsoft.com')
is_valid_email('bob#example.com')
is_valid_email('mr-bob@example.com')
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')

# 2. 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

def name_of_email(addr):
    # re_em_name = re.compile(r'([<]?[a-zA-Z\s]+)[>]?\s\w@[a-z]*.[a-z]{3}$')
    re_em_name = re.compile(r'<?([a-zA-Z\s]*)>?[\sa-z]*@[a-z]*.[a-z]{3}$')
    m7 = re_em_name.match(addr).groups()
    print(m7)

name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
