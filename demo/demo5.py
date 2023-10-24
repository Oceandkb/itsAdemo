# chao
# 时间：2023/9/18 8:29 下午

# 使用list和tuple


# list 列表、有序，列表的插入、追加、删除、按照索引查询
list = ['daming', 'lingling', 'tom', 'lily']
print(len(list)) # 输出列表的长度
print(list[2])   #访问列表某个索引位置的值
print(list[-1])  #访问列表中最后一个索引的值
list.append('adam') # 追加元素到列表末尾
print(list)
list.insert(2, 'biber') # 插入元素到指定索引位置
print(list)
list.pop() # 删除列表末尾的元素
print(list)
list.pop(2) # 删除指定位置的元素
print(list)
list[1] = '1+1' # 替换指定位置的元素
print(list)

list.append([1, 2])
print(list)
list.insert(3, [3, True])
print(list, len(list))
print(list[3][1])


L = [['apple', 'google', 'microsoft'], ['java', 'python', 'ruby', 'php'], ['adam', 'bart', 'lisa']]

print(L[0][0])
print(L[1][1])
print(L[2][2])


# 元组 tuple





