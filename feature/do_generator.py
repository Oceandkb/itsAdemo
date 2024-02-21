# chao
# 时间：2023/12/4 10:42
# 生成器：一边循环，一边计算的机制，称为生成器

# 将列表生成式的[]改成()，就可以创建一个生成器
g = (x * x for x in range(10))
print(g) # 直接打印生成器是一个generator的类型
print(next(g)) # 使用next打印生成器中的元素
# 如果要打印很多g的元素，使用for循环才是正确方法
for G in g:
    print(G)

# 使用函数来输出生成器内容
# 斐波拉契数列：除了第一个数和第二个数，其他的数都可以通过前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b # 定义了计算规则
        n = n + 1
        print(n)
    return 'done'

# print(fib(9))

# 但是fig函数还不是生成器，把print(b)改成yield b，得到一个生成器
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # 如果一个函数中包含yield关键字，那么这个函数就是一个生成器，调用会返回一个生成器
        a, b = b, a + b
        n = n + 1
        # print(n)
    return ('done')

print(fib_g(9))

for n in fib_g(9):
    print(n)
# 但是使用for循环输出generator中的值，没办法输出return的值

# generator和普通函数的区别是：
# 普通函数是遇到return或者最后一行语句返回
# generator遇到yield就会返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3

o = odd() # 调用生成器函数时，要先生成一个generator函数对象
next(o) # 然后使用next输出
next(o)
next(o)
# 如果直接调用generator函数
next(odd()) # 这样每次调用都会生成一个新的对象，都输出第一个值
next(odd())

# 总结
# 列表生成式[]和生成器()的括号不同
# 输出生成器值的时候，使用next
# 如果输出很多值，使用for循环遍历generator中的值
# 在函数中如果包含yield关键字，则这个函数是生成器函数
# 生成器函数遇到yield就会返回
# 在调用生成器函数时，需要先创建一个生成器对象，然后使用next输出

# 练习
def triangles():
    L = [1]
    S = []
    while True:
        yield L
        L = [1] + S + [1]
        S = []
        for i in  range(len(L)-1):
            S.append(L[i] + L[i + 1])

# for t in triangles():
#     print(t)


def generate_pascal_triangle(rows):
    '''

    :param rows: 传入需要生成三角的层数
    :return:
    '''
    row = [1]
    yield row # 先使用yield输出第一行

    # 创建一个循环，循环计算除第一层的，每一层的元素
    for l in range(rows - 1):
        print('循环的第',_, '层')
        next_row = [1] # 每一层循环时，创建一个next_row对象，赋予初始值1，作为第一个不变的元素

        # 嵌套一个循环，来计算每一层除去首尾中间的元素
        for i in range(len(row) - 1):
            print('在第', _, '层中，i = ', i)
            next_row.append(row[i] + row[i + 1]) # 将上一行两个相邻的元素添加到next_row中

        next_row.append(1) # 最后给next_row添加最后一个不变的元素1
        row = next_row # 将next_row赋值给row
        yield row

# 测试代码
triangle_generator = generate_pascal_triangle(5)
for row in triangle_generator:
    print(row)

