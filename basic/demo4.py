# chao
# 时间：2023/9/15 5:08 下午
# 字符编码

# unicode和utf-8的编码规则

# python3 使用unicode编码，字符串可以支持多种语言
print('中文、english字符串')

# ord函数，获取字符的十进制整数表示
print(ord('a'))
print(ord('中'))

#char函数，转换编码为对应的字符
print(chr(23145))

#占位符
# %形式
print(('hello, %s %d') % ('daming', 101))
# format()
# f-string()

#计算第二次分数相对于第一次增长了多少百分点，使用字符串格式化输出
a = 72
b = 85
r = b-a
d = (r/a)*100
print(f'小明的成绩提升了 {d:.2f}%')
