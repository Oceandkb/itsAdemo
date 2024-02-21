# chao
# 时间：2023/12/1 10:13
# 迭代
# 使用for循环，遍历整个list或者tuple，称为迭代
# for循环还可以用于可迭代对象上

# 迭代没有下标的dict，可以对key进行迭代，但是没有下标，迭代结果顺序不确定
d = {'a': 1, 'b':2, 'c': 3}
for key in d:
    print(key)

# 对dict的value进行迭代
for value in d.values():
    print(value)
# 或者，迭代key和value
for k, v in d.items():
    print(k, v)

# 字符串也是可迭代的对象
for ch in 'hahaha':
    print(ch)

# 判断一个对象是否为可迭代对象
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 4], Iterable))
print(isinstance(123, Iterable)) # int不能被迭代

# 对list实现下标循环
for i, value in enumerate([1, 3, 4]):
    print(i, value)

# 在for循环中同时引用两个变量
for x, y in [(1, 1), (2, 2)]:
    print(x, y)

# 练习
# 使用迭代查找list中的最小和最大值，返回一个tuple
def findMinAndMax(L):
    if L == []:
        return (None, None)
    mi = L[0]
    ma = L[0]
    for v in L:
        if v < mi:
            mi = v
        if v > ma:
            ma = v
    return (mi, ma)
print(findMinAndMax([7, 1, 3, 9, 5]))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 想法对了，就是迭代比较每一个值，小的就赋值给一个变量，但是没写对，吗的

# 总结：
# 使用for循环对list、tuple或者其他的可迭代对象进行迭代
# dict可以迭代key，使用v in d.values()可以迭代值，使用k, v in d.item()可以迭代键值对
# 使用collection.abc的Iterable类可以判断对象是否可以迭代
# 使用enumerate方法可以返回list的下标和值
