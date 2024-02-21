# chao
# 时间：2023/9/14 2:39 下午
# 数值类型


print(123) #整数类型 int
print(1.0, type(1.0)) #浮点型 float
print('fxxk') # 打印字符串 str
print('\"fxxk\"') # 当需要打印的字符串中，包含''或者""，需要用转义字符\
print('\\fxx\\k') # 当然，转义字符本身也需要被转义，如：\\
print('''1
2
3 ''')
print(r'''hello,\n
world''')

print(True, type(True)) # 布尔值 bool
# 布尔值运算： 与、或和非
if 1>2 and 2>3:
    print(True)
else:
    print(False)

if 1>2 or 2>1:
    print(True)

if not 1>2:
    print(True)
