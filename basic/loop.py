# chao
# 时间：2023/11/29 10:53
# 循环

# for循环
# 使用for循环打印列表中的值
names = ['chao', 'qi', 'mai', '1+1']
# for x in ...就是把每个元素都带入到x中，执行缩进的语句
for name in names:
    print(name)

# 计算1-10的整数和
sum = 0
for i in range(11): # range()返回一个小于传入值的整数列表
    sum = sum + i
    print(sum)

# while循环：只要条件满足，一直循环，条件不满足，结束循环
# 计算100以内奇数的和
sum0 = 0
i = 1
while i <= 100:
    sum0 = sum0 + i
    i = i + 2
print(sum0)

# 利用循环，依次对list中的每个名字打印hello，xxx！
na = ['daming', 'lingling', 'amy']
for n in na:
    print(f'hello, {n} !')

# 使用break语句可以提前推出循环
# 打印1-100的数字，提前结束
a = 0
while a <= 100:
    if a > 10:
        break # 加入a》10的判断，如果a》10，结束循环
    print(a)
    a = a + 1

# 使用continue语句跳过当前循环，直接进行下一次循环
# 使用continue语句，只打印10以内的奇数
b = 0
while b < 10:
    b = b + 1
    if b % 2 == 0:
        continue # 如果b可以被2整除，那么跳过这次循环，执行下一次
    print(b)

# 总结
# 两种循环方式：for和while
# for是赋值循环，while是条件循环