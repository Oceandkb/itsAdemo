# chao
# 时间：2023/11/29 11:21
# 字典

# dict代表字典，使用key-value进行存储，具有极快的查找速度
# 定义一个dict，并查找dict中的value
d = {'daming': 95, 'amy': 80, 'lingling': 98} # 定义用花括号
print(d['amy']) # 查找时使用[]

# 通过key向dict中添加value
d['chao'] = 90 # 插入一个新的键值对
d['amy'] = 78 # 更改已有key的value
print(d)
# 如果插入的key是不存在的，则会抛出异常
# 所以使用in或者get的方法查看key是否存在
print('11' in d) # 返回False或者True
print(d.get('22', 'key is not exist')) # key不存在时，可以指定返回内容

# 删除key：pop(key)
d.pop('chao')
print(d)

# 总结
# dict创建用{}，查询用[]
# dict查询速度快，但是占用空间大，和list正好相反，是一种使用空间换时间的方法
# dict的key必须是不可变对象，例如字符串和整数都可以，但是list是可变的，不能作为dict的key
