import os
# 练习
# 1. 利用os模块编写一个能实现dir -l输出的程序



# 2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''
查看当前目录和子目录
过滤包含自定义字符串的文件

看到评论定义一个方法，方法中入参路径和字符串
'''
fd = os.path.abspath('.') # 当前目录
kd = os.listdir(fd) # 获取当前目录下的所有子目录和文件
# listdir返回的是一个列表
# 遍历这个列表
for item in kd:
    kd_path = os.path.join(fd, item)
    if os.path.isdir(kd_path):
        # 判断是否为子目录
        print(kd_path)

search_str = 'dir'
f = [x for x in os.listdir(fd) if os.path.isfile(x) and search_str in x]
print(f)
for file in f:
    relative_path = os.path.relpath(file, )
    print(relative_path)