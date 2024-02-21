# chao
# 时间：2023/11/29 12:12
# 定义函数

def my_abs(x):
    # 自己定义的函数，可以检查传参数量的错误，但是无法检查传参类型的错误
    # 使用isinstance方法，判断x是否是属于int或者float类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(23))

# 定义一个空函数
def non(age):
    if age > 18: # 如果有需要返回内容的代码，pass可以保证代码运行
        pass # 使用pass语句来占位，让代码不会报错

# 函数返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(12, 34, 45)
print(x, y)

# 实际上，当函数return多个值时，调用函数返回的值是以tuple的形式返回的
r = move(11, 33, 44)
print(r)


# 总结：
# 定义函数使用def
# 自己定义的不能检查传参的类型，可以使用isinstance来检查
# 函数可以返回多个值，返回多个值时，使用tuple的方式返回
# 没有返回语句时，自动返回None

def quadratic(a, b, c):
    if not isinstance(a, int):
        raise TypeError
    if not isinstance(b, int):
        raise TypeError
    if not isinstance(c, int):
        raise TypeError
    o = b ** 2 - 4 * a * c
    if o < 0:
        return None
    else:
        x0 = (-b + math.sqrt(o)) / 2 * a
        x1 = (-b - math.sqrt(o)) / 2 * a
        return x0, x1

print(quadratic(2, 3, 1))