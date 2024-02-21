#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/1/17 16:01
@Author : chao
@File   : err_solu.py
'''
# 错误处理
# try...except...finally 错误处理机制

# try
try:
    print('try...')
    r = 10 / 0 # 先执行try，如果有错误，跳出，去执行except部分，最后执行finally
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally: # 可有可无，如果有就一定会执行
    print('finally...')
print('END')
'''
输出如下：
try...
except: division by zero
finally...
END
'''

# except语句用于处理错误，所以有多种不同的except类型
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
# 使用两个except去处理可能出现的error
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
# 也可以在exception后加上else语句，输出没有error的情况
else:
    print('no error')
finally:
    print('finally...')
print('END')

# python的所有error都是class，全部继承于BaseException
# 所以except不仅仅处理该类型的错误，也会处理子类的错误
try:
    r = 10 / int('a')
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# 上边这种情况，永远不会由UnicodeError处理,因为它是ValueError的子类
# 所有的错误类型和继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# try...except...可以跨层级调用
def f1(s):
    return 10 / int(s)
def b1(s):
    return f1(s) * 2
def main():
    try:
        b1('0')
    except Exception as e:
        print('Exception:', e)
    finally:
        print('finally')
# 在调用main函数的时候，发现f1的错误也可以直接处理，不需要单独为f1或者b1去写try...except...
m = main()

