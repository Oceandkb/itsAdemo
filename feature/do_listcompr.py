# chao
# 时间：2023/12/1 11:58
# 列表生成式 list comprehensions

#创建1-10的list
l = list(range(1, 11))
print(l)

# 生成[1x1, 2x2, ..., 10x10]的list
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 使用列表生成式
# 列表生成式中，要生成的元素放到for前边，后边写for循环
a = [x * x for x in range(1, 11)]
print(a)

# for循环后还可以加上if判断
b = [x * x for x in range(1, 11) if x % 2 == 0]
print(b)

# 也可以使用两个循环
c = [o + w for o in 'abc' for w in 'sdf']
print(c)

# 使用列表生成式输出当前目录下所有文件和目录名称
import os
d = [d for d in os.listdir('.')]
print(d)

# 列表生成式也可以使用for循环遍历两个变量
dic = {'a': 'A', 'b': 'B', 'c': 'C'}
dd = [x + '=' + y for x, y in dic.items()]
print(dd)

# 把字符串中的字母变成小写
bb = ['HRRHRHRHRHHRHR']
ss = [s.lower() for s in bb]
print(ss)

# 在使用列表生成式时，for后边使用if，不能加else，因为if做为一个筛选条件，加else就不能筛选了
# 但是如果在for之前写if，就必须加上else，因为for之前是一个表达式，必须要根据x计算出一个结果
q = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(q)

# 总结：
# 列表生成式中可以使用for循环，for之前代表生成的内容，for代表循环
# 可以循环多个变量
# for后边可以加if筛选，但是不能加else
# for之前使用if，必须有else，组成一个表达式

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)