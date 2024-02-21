# chao
# 时间：2023/11/29 11:21
# set 集合

# set是一组key的集合，但是不包含value，key不能重复
# 创建set，需要使用list作为key的输入，重复key会被自动过滤
s = set([1, 1, 3, 2, 3])
print(s)

# 通过add(key)，对set添加元素
s.add(4)
print(s)

# 通过remove(key)，删除set中的元素
s.remove(4)
print(s)

# set在数学意义上，可以看成是无序的无重复元素的集合，可以进行集合运算
s1 = set([1, 32, 4, 5])
s2 = set([2, 34, 5, 65])
print('s1和s2的交集为：', s1 & s2)
print('s1和s2的并集为',s1 | s2)

# set同样不能放入可变对象，放入list会报错
# l = [1, 3]
# s3 = set([l, 1, 3])

# 总结：
# set和dict原理一样，只是set不存放value
# set可以作为集合进行集合运算