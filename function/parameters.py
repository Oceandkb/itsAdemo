# chao
# 时间：2023/11/29 12:12
# 函数的参数

# 位置参数
def power(x):
    return x * x
# 当想要计算x的n次方时，可以添加一个参数n来指定幂
def powern(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powern(5, 3))
# 对于power和powern函数，x和n作为必须要传的参数，叫做位置参数，多个参数时按照顺序传入

# 默认参数
# 在定义函数时，把参数n的默认值设成2，在调用时可以只传a，正常执行
# 如果想要传入其他的n的值，就需要手动传参了
def power0(a, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * a
    return s
# 在设置默认参数时，需要注意：
# 1. 默认参数放在必须参数后边（因为调用时，传参顺序时从前开始对应的）
# 2. 把变化小的参数放到后边，作为默认参数，方便函数调用
# 3. 默认参数一定要指向不变对象

# 可变参数：当传入的参数不确定的时候，可以传入1个2个，或者多个
def calc(*numbers): # 参数作为一个list或者tuple传入，在参数前加一个*号，参数接收到的是一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print('calc', calc(1, 3, 4))
# 如果想把已有的list或者tuple传入，传入时在list或者tuple前加上*号即可
num = [1, 4, 5]
print(calc(*num))

# 关键字参数
# 可以传入0个或者多个含有参数名的参数，关键字参数在函数内部自动组装成一个dict
# 关键字参数可以扩展函数的功能
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('daming', 14)
# 传参时可以传入新的键值对
person('amy', 14, country = 'usa')
# 也可以使用已有的dict传参
extra = {'country': 'beijing', 'job': 'coder'}
person('tom', 24, country = extra['country'])
person('luke', 25, **extra) # 把整个dict传给kw参数

# 命名关键字参数，用于限制关键字参数的名字
def person1(name, age, *, country, job): # 在命名关键字参数前要加上*,作为识别*后边的参数为命名关键字参数
    print(name, age, country, job)

person1('mai', 23, country='beijing', job='cat')
# 注意，如果函数定义了命名关键字参数，传参时需要加上参数名称
# 如果参数中已经有一个可变参数，其后的参数都认为是命名关键字参数
def person2(name, age, *cats, job):
    print(name, age, cats, job)

person2('chao', 26, [1, 3, 4], job='cat')

# 参数组合
# 上边学习的位置参数、默认参数、可变参数、关键字参数和命名关键字参数，都可以组合使用
# 顺序必须是：位置参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b, c=1, *args, **kw):
    print(a, b, c, 'args=', args, 'kw=', kw)

f1(1, 3, 3,(23, '好的'), bbb = '123')
args = (1, 3, 4, 5)
kw = {'d': 99}
f1(*args, **kw) # 任何形式的函数都可以用func_name(*arg, **kw)来调用

def f2(a, b):
    print(a, b)

z = [1, 3]
f2(*z)

# practice
def mul(*number):
    result = 1
    for num in number:
        result = num * result
        print(result)
mul(5, 6, 7)

# 总结
# 1. 函数的参数有位置参数、默认参数、可变参数、关键字参数、命名关键字参数
# 2. 默认参数可以简化调用函数的语句，默认参数需要放到位置参数之后
# 3. 可变参数定义时前边要加*，可以使用已有的list或者tuple传入，*list，也可以直接传入list或者tuple
# 4. 关键字参数，**kw，在函数内部组装为dict
# 5. 命名关键字参数，用*,来表示后边的都是命名关键字参数，传参时必须要加上参数名