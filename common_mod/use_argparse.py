#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/29 10:19
@Author : chao
@File   : use_argparse.py
'''
import sys
# 获取命令行的参数
# print(sys.argv)
# 打印从命令行传递的所有参数，输出是字符串列表
# 第一个元素是脚本命令，后续元素就是传递给脚本程序的参数
# source1 = sys.argv[1]
# source2 = sys.argv[2]
# print(source1, source2)


# 当参数复杂时，可以使用内置的argparse库
# 定义好各个参数类型后，它能直接返回有效参数

# 编写备份mysql数据库的命令行程序，需要输入如下参数
# host, port, user, password, gz, outfile(文件备份位置)
import argparse

def main():
    # 定义一个ArgumentParser实例：
    parser = argparse.ArgumentParser(
        prog = 'backup', # 程序名
        description='Backup MySQL database.', # 描述
        epilog='Copyright(r), 2023' # 说明信息
    )
    # 定义位置参数
    parser.add_argument('outfile')
    # 定义关键字参数
    parser.add_argument('--host', default='localhost')
    # 端口，int类型
    parser.add_argument('--port', default='3306', type=int)
    # 允许拥护输入简写的-u：
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true', 意思是出现-gz表示True：
    parser.add_argument('-gz', '--gzcompress', action='store_true',
                        required=False, help='Compress backup files by gz.')

    # 解析参数
    args = parser.parse_args()

    # 打印参数
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()

# 这个没搞懂啥玩意