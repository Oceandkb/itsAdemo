# chao
# 时间：2024/1/10 18:22

'a test module (这是一个文档注释'
__author__ = 'chao' # 使用__author__变量把作者名称写到模块内

import sys

def test():
    args = sys.argv # 用list存储命令行的所有参数，至少一个元素，为该py文件的名称
    if len(args)==1:
        print('Hello world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1]) # %s的作用就是替换%后边的元素
    else:
        print('Too many arguments!')


if __name__=='__main__':
    test()
