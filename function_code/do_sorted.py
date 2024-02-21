# chao
# 时间：2024/1/10 11:09
# sorted算法，排序

# 使用sorted函数可以对list中的元素进行排序
print(sorted([1, 34, 2, 345, 32]))

# sorted函数也是高阶函数，可以接受一个key函数来实现自定义排序
# 按照绝对值大小排序
print(sorted([-11, -3, 45, -889], key=abs))

# 对字符串排序，按照ASCII码
print(sorted(['Zoo', 'Credit', 'maixuanfeng']))
# 如果忽略大小写，可以使用key来将所有字符串改为大写或者小写
print(sorted(['Zoo', 'Credit', 'maixuanfeng'], key=str.lower))
# 传入reverse参数，倒序输出
print(sorted(['Zoo', 'Credit', 'maixuanfeng'], key=str.upper, reverse=True))

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
def by_name(t):
    nt = t[0]
    print(nt)
    return nt

print(sorted(L, key=by_name))
print(sorted(['Bob', 'Adam', 'Bart', 'Lisa']))

# 再按成绩从高到低排序
def by_score(t):
    st = t[1]
    return st

print(sorted(L, key=by_score, reverse=True))

