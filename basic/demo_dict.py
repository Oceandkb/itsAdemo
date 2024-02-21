# chao
# 时间：2023/10/20 16:21


d = {'麦旋风': '狸花猫', '1+1': '橘猫'}
d['大宝'] = '墨西哥蛋龟'
if '黄缘' in d:  # 判断key是否在dict中
    print(d['黄缘'])
else:
    print('false')

s = d.get('小橘', -1)
print(s)

# 删除key，pop()
d.pop('大宝')
print(d)

