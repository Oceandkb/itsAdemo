# chao
# 时间：2023/10/12 14:46

height = 1.75
weight = 80.5

bmi = weight/height ** 2  #a ** 2 计算平方
print(bmi)

if bmi<18.5:
    print('小明的体重过轻')
elif bmi>18.5 and bmi<25:
    print('正常')
elif bmi>25 and bmi<28:
    print('过重')
elif bmi>28 and bmi<32:
    print('肥胖')
else:
    print('严重肥胖')