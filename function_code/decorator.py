# chao
# 时间：2024/1/10 16:11
# 装饰器
# 在代码运行期间动态增加功能的方式叫做装饰器
# decorator本质上是一个返回函数的高阶函数

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

from datetime import datetime
@log # 将@log放到函数now的定义上，相当于now = log(now)
def now():
    print(datetime.now())

now()