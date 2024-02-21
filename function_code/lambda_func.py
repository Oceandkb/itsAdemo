# chao
# 时间：2024/1/10 16:03
# 匿名函数
# 在高级函数中传入函数时，可以不用显式地定义，可以直接传入匿名函数方便

# 计算x的平方
m = map(lambda x: x * x, [1, 3, 4, 5])
print(list(m))
# 其中lambda代表匿名函数，冒号前的x为参数
# 匿名函数不能写return，只有一个表达式，结果就是返回值
# 匿名函数可以赋值给变量
f = lambda x: x + 1
print(f(3))

# 匿名函数可以作为结果返回
def no_func():
    return lambda x: x + 4

n = no_func()
print(n(4))

# 练习
# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

