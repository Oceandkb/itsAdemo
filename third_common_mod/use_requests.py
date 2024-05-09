#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/8 17:22
@Author : chao
@File   : use_requests.py
'''
import requests
# 一行代码就能访问一个get请求
r = requests.get('https://www.python.org/events/python-events/')
print(r.status_code)
# print(r.text)

# 对于带参数的url，传入一个dict作为params参数
# r1 = requests.get('https://movie.douban.com/subject/', params={'q': 'python'})
# print(r1.status_code)
# 这个是模拟的，url不是真是存在的

print(r.encoding) # requests自动检测编码，可以使用encode属性查看

# requests的方便之处在于，对于特定的响应类型，可以直接获取，比如json
r1 = requests.get('http://www.kuaidi100.com/query?type=快递公司代号&postid=快递单号')
print(r1.status_code)
print(r1.text)
print(r1.json())
# 注意：返回内容必须是json格式，如果不是会报错

# 当需要传入headers的时候，可以传入一个dict作为参数

# post请求，只需要使用post方法，然后传入data作为入参

# 如果入参是json格式，可以直接传入json参数
# params = {
#     'key': 'value'
# }
# r3 = requests.post(url, json=params)

# 如果上传文件需要更复杂的编码格式，但是requests把它简化成files参数
# upload_files = {'file': open('report.xls', 'rb')} # rb代表的是二进制读取模式，必须使用
# r4 = requests.post(url, files=upload_files)

# requests也可以直接访问put、delete请求
#


