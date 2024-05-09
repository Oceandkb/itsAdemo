#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/7 17:23
@Author : chao
@File   : use_urllib.py
'''

# Get
from urllib import request, parse

with request.urlopen('https://blog.mookio.net/') as f:
    # 利用request模块中的urlopen方法访问一个链接（有些网页会反爬虫，所以要加user agent）
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# 如果想要模拟浏览器发送get请求，就要使用Request对象
# 通过在Request对象添加HTTP头，可以把请求伪装成浏览器

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML,'
                             ' like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# 使用add_header方法，添加一个代理，仿造是iphone去访问网页
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# Post
# 发送post需要有data，也就是入参
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode(
    [
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerfer', 'https://passport.weibo.cn/singin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ]
)

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)'
               ' Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data = login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# Handler
# 复杂一点：通过Proxy（代理）去访问网站，需要利用ProxyHandler


