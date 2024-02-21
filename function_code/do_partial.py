# chao
# 时间：2024/1/10 18:06
# 偏函数: functools.partial
# 把一个函数的某些参数给固定住（设置默认值），返回一个新的函数

print(int('123456')) # int函数，将字符串转换为整数，默认十进制
print(int('1000111', base=2)) # 如果想要转换为二进制，就传入base参数
# 使用partial方法，创建一个偏函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1001101'))

# 创建偏函数可以接受函数对象、*args和**kw这三个参数

