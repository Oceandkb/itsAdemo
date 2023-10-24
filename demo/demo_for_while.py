# chao
# 时间：2023/10/16 16:26

# for
brands = ['yy', 'victor', 'lining']
for brand in brands:
    print(brand)


sum = 0
list = [1,2,3,4,5]
for x in list:
    sum = sum + x
print(sum)

sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)

# while
sum2 = 0
n = 99
while n>0:
    sum2 = sum2 + n
    n = n - 2
    print(sum2)

names = ['bart', 'lisa', 'adam']
for name in names:
    print('hello,' + name + '!')

a = 0
while a<100:
    if a > 10:
        break
    print(a)
    a = a+1
print('end')

# 输出10以内的奇数
b =0
while b<10:
    b = b + 1
    if b % 2 == 0:  # 如果b能被2整除，则继续循环，如果不能，则退出循环，打印b
        continue
    print(b)