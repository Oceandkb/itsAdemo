#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/7 21:03
@Author : chao
@File   : test_urllib.py
'''

# 练习
# 利用urllib读取JSON，然后将JSON解析为Python对象：
from urllib import request
import json
def fetch_data(url):
    # 思路
    # 先访问url，获得user agent
    # 通过header代理模拟去访问url
    # 使用with语句来实现上下文管理
    # 获取返回值
    # 将json转换为python对象，字典
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                                  '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69')
    with request.urlopen(req) as h:
        print('Status:', h.status, h.reason)
        data = h.read()
        data_d = json.loads(data)
    return data_d

result = fetch_data('https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20240501&st=env')
print(result)
print(type(result))
assert  result['injector_basename'] == 'sodar2'
print('ok')