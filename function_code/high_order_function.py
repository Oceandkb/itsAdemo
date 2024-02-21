# chao
# 时间：2024/1/9 15:30
# 高阶函数

# 变量可以指向函数
print(abs(-10))
# 可以通过调用函数得到的值赋值给变量，函数也可以赋值给变量
f = abs
print(f(-20))

# 函数名也是变量
# abs = 10
# print(abs(-10)) # 会报错，因为abs被指向了一个int常量

# 传入函数
# 函数的参数可以接受变量，也可以接受另一个函数作为参数，这种就叫做高阶函数
def add(x, y, f):
    return f(x) + f(y)
# f对应的传参为abs这个函数
print(add(-5, -9, abs))

# map函数
# map函数接受两个参数：函数和iterable
# 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6])
# r是一个iterator，需要是用list来输出打印r的值
print(list(r))

s = map(str, [1, 3, 4, 6, 6])
print(list(s))

# reduce函数
# 和map类似，reduce把一个函数作用在一个序列上
# reduce把结果继续和序列的下一个元素做累计计算

from  functools import reduce
# 求和
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 4, 5, 6]))

# 把[1, 3, 4, 5, 6]变换成整数[13456]
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 4, 5, 6]))

# 配合map，将str转换为int
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
    return digits[s]
print(reduce(fn, map(char2num, '1234')))

# str2int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


# practice
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    new = ''
    # 使用enumerate去获取字符串的索引位置和对应的字符
    for i, n in enumerate(name):
        if i == 0:
            new = new + n.upper()
        else:
            new = new + n.lower()
    return new

print(normalize('eLla'))

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def pro(x, y):
        return x * y
    return reduce(pro, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数
# 把字符串'123.456'转换成浮点数123.456

