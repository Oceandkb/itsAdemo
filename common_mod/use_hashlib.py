#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/30 11:18
@Author : chao
@File   : use_hashlib.py
'''

# 摘要算法
import hashlib

# md5是常见的摘要算法，速度快，生成结果是固定128bit/16字节，通常用一个32为的16进制字符串表示
md5 = hashlib.md5()
# 通过update将utf-8编码的字符串传给md5对象
md5.update('my heart will go on'.encode('utf-8'))
print(md5.hexdigest()) # hexdigest方法获取哈希值的16进制

# sha1也是一种摘要算法
# 结果是160bit/20字节，用40位的16进制字符串表示
# sha256和sha512更安全，但是也更慢
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python'.encode('utf-8'))
print(sha1.hexdigest())

# ⚠️使用不同的摘要算法有可能获取相同的加密哈希值，但是非常困难



# 练习
# 根据用户输入的口令，计算出存储在数据库中的md5口令
def calc_md5(password):
    mdd5 = hashlib.md5()
    mdd5.update(password.encode('utf-8'))
    return mdd5.hexdigest()

print('密码的加密值为：%s' % calc_md5('1233445455'))

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    # 将password使用md5加密
    # 将user和加密后的password和db中的值对比
    # 匹配返回True，不匹配返回False
    m5 = hashlib.md5()
    m5.update(password.encode('utf-8'))
    h_password = m5.hexdigest()
    if user in db:
        db_password = db[user]
        if h_password == db_password:
            return True
        else:
            return False
    else:
        print('the login user did not register in our website')

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 加盐操作
def calc_md5(password):
    return get_md5(password + 'the-Salt')

# 练习

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

import random
def get_md5(user, pws):
    md5 = hashlib.md5()
    md5.update((user.username + pws + user.salt).encode('utf-8'))
    return md5.hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(self, pws = password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}



def login(username, password):
    user = db[username]
    return user.password == get_md5(user, password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
