# chao
# 时间：2023/11/30 11:18
# 切片

# 取list或者tuple中的某几个元素
l = ['chao', 'qi', 'mai', '1+1']
print(l[0:3])
# 用[a:b]形式来取列表元素，a代表开始索引，b代表结束索引，包括a，不包括b
# 如果索引从0开始，可以省略为[:b]
print(l[-2:-1])
# 也可以从尾部取切片，但是注意，这样的开始是-1，包括-1，不包括-2
n = list(range(1000))
print(n)
print(n[:11])
print(n[-11: -1])
# 也可以加上步长，相隔n个步长取值
print(n[:20:3])
# ''字符串也可以看成list，也可以进行切片
print('string'[0:3])

# 练习
# 自己写的，实在写不出来了，只能问chatgpt了
# def trim(s):
#     l = list(s)
#     i = 0
#     while i < len(l):
#         if l[i] == ' ':
#             l.pop(i)
#         else:
#             i = i + 1
#     s = ''.join(l)
#     print(s)
# trim('  12 3 ')

def trim(s):
    start = 0
    end = len(s) - 1
    # 从前边找非空格字符的索引
    while start <= end and s[start] == ' ':
        start += 1
    # 从后边找非空格字符的索引
    while end >= start and s[end] == ' ':
        end -= 1
    # 返回非空格宗福的索引切片
    return s[start:end+1]

print(trim('     hello    world    '))

# 我自己的想法是，从两端循环取找空格字符，然后删掉，但是没有用到切片
# 并且写的过程中删除元素后，list的长度就变了，一直list out of range
# 使用切片的方式，chatgpt比较简单清晰，从两端找非空的索引，然后用切片输出

# 总结：
# 对list或者tuple切片取值