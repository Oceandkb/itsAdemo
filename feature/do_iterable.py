# chao
# 时间：2023/12/4 20:12
# 迭代器
# 可以作用于for循环的有list、tuple, set, dict, string等
# 还有generator，这些都可以称之为可迭代对象：Iterable

# 使用isinstance判断对象是否为iterable
from collections.abc import Iterable
from collections.abc import Iterator
print(isinstance([], Iterable))
print(isinstance('dwefr', Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({1: 1, 2: 2}, Iterable))

# 可以使用next()方法，不断返回下一个值的对象，称为迭代器
# 但是list、dict、str都是iterable，但不是iterator
# 因为iterator表示的是一个数据流，我们并不能提前知道序列的长度
# 使用iter()方法，将iterable变成iterator
print(isinstance(iter(['abc']), Iterator))


# 总结：
# 可以应用与for循环的，都是iterable
# 可以应用与next的，都是iterator

from d2l import torch as d2l


