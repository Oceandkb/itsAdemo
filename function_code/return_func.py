# chao
# 时间：2024/1/10 15:05
# 返回函数
# 高级函数还可以把函数作为结果值返回

# 定义一个求和的返回函数
def lazy_sum(*args):
    '''
    在lazy_sum中的定义了函数sum
    并且内部函数sum可以引用外部函数的参数和局部变量
    当lazy_sum函数的返回函数sum时，相关的参数和变量都会保存在返回的函数中（闭包）
    :param args:
    :return:
    '''
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 当调用lazy_sum时，返回的并不是结果，而是sum函数
f = lazy_sum(1, 3, 5, 5, 6)
print(f)
# 调用f时才会返回结果
print(f())

f1 = lazy_sum(1, 3 ,4)
f2 = lazy_sum(1, 3, 4)
# f1==f2是false的，即使入参相同，两次调用都会返回一个新的函数，也是不相同的
print(f1 == f2)

# 闭包
# ⚠️返回闭包时牢记：返回函数不要引用任何循环变量， 或者后续会发生变化的变量

# nonlocal
# 如果时内部函数只是读取外层变量，一切正常
def inc():
    x = 0
    def fn():
        return x + 1
    return fn

i = inc()
print(i())

# 如果在内部函数中对外层变量赋值，则会报错
# def inc1():
#     x = 0
#     def fn():
#         x = x + 1
#         return x
#     return fn
#
# i = inc1()
# print(i())
# 因为对外层变量赋值的话，会把x当作内部函数fn的局部变量
# 但是x作为内部函数fn的局部变量的话是没有初始化的，所以会报错
# 当我们只是想要在内部函数中访问外层函数的变量时，可以加上nolocal的声明
def inc2():
    x = 1
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

i = inc2()
print(i())

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')