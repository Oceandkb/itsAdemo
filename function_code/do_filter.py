# chao
# 时间：2024/1/9 20:08
# filter函数用于过滤序列

# 入参和map相同，不同的是，filter是将传入的函数依次应用于蓄力的每个元素，根据返回的True和False来决定元素的去留
# 删除list中的偶数
def is_odd(n):
    return n % 2 == 1
l = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))
print(l)
# 删除一个序列中的空字符串
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['', '1', '334', ''])))

# 用filter求素数（大于1的自然数中，除了1和本身没有其他的因数）
# 埃氏筛法
def _odd_iter():
    '''
    构造一个从3开始的奇数序列（把2的倍数全部都剔除）
    :return: 返回的是一个无限序列
    '''
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    '''
    定义一个筛选函数
    :param n:
    :return:
    '''
    return lambda x: x % n > 0

def primes():
    '''
    定义一个生成器，不断返回下一个素数
    :return:
    '''
    yield 2
    it = _odd_iter() # 使用_odd_iter方法生成初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新的素数序列

# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
# 请利用filter()筛选出回数

def is_palindrome(n):
    pass