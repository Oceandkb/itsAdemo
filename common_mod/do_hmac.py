#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/30 15:41
@Author : chao
@File   : do_hmac.py
'''

# Hmac算法就是相当于hashlib中的salt方法
# 通过一个标准算法，在哈希时，将key（salt）加入其中
# Hmac有标准的算法，代替自定义的salt方法
import hmac

# 需要注意的是，传入的message和key都是bytes类型
message = b'Hello World!'
key = b'secret'
# new方法，传参为key、message（salt）、哈希算法
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

# 练习
# 将hashlib转换成hmac

import random
def hmac_md5(key, s):
    h = hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5')
    return h.hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}



def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
