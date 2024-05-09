#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/4/24 20:56
@Author : chao
@File   : use_datatime.py
'''

# datetime是处理日期和时间的库
from datetime import datetime, timedelta, timezone # 从datetime模块中导入datetime类

# 获取当前的日期和时间
now = datetime.now() # 获取当前日期和时间
print(now, type(now))

# 输出指定日期和时间
dt = datetime(2019, 8, 28, 9, 30, 8)
print(dt)

# 将datetime转换为timestamp
# 计算机中，时间用数字表示，1970-1-1的00:00:00 UTC+00:00的时刻称为epoch time，记为0
# 当前时间就是相对于epoch time的秒数，称为timestamp
# timestamp的值和时区无关
dtt = dt.timestamp()
print(dtt, type(dtt)) # timestamp是float类型

# 将timestamp转换为datetime
t = 1566955808.0
print(datetime.fromtimestamp(t))
# timestamp和datetime有个区别就是datetime有时区的概念，所以转换后的datetime是本地时区
print(datetime.utcfromtimestamp(t)) # timestamp也可以转换为格林威治时间

# 将str转换为datetime
cday = datetime.strptime('2019-11-20 17:22:09',
                         '%Y-%m-%d %H:%M:%S') # 后边的字符串规定了日期的格式
# 注意，str转换后的datetime是没有时区概念的
print(cday)

# 将datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
# 可以直接使用+-运算符，需要导入timedelta类
n = now + timedelta(hours=2)
n1 = now + timedelta(days=1)
n2 = now - timedelta(hours=8)
print('n 是 %s' % n)
print('n1 是 %s' % n1)
print('n2 是 %s' % n2)

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
n3 = datetime.now()
print('n3 是 %s' % n3)
dtz = now.replace(tzinfo=tz_utc_8)
print('转换为UTC时间为：%s' % dtz)
# 没搞懂啥意思

# 时区转换
utc_dt = (datetime.utcnow().replace(tzinfo=timezone.utc))
# 先获取当前utc的当前时间，然后使用replace强制设置时区为UTC+0:00
print(utc_dt)
# 使用astimezone将时区转换为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# 时区转换的关键是，一开始一定要获取当前时间然后强制转换为UTC+0:00，replace(tzinfo=timezone.utc))
# 然后再去使用astimezone去更换时区


# 小结
# 存储datetime最佳方法是转换为timestamp，因为与时区无关

# 练习
import re
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime('2015-1-21 9:01:30', '%Y-%m-%d %H:%M:%S')
    pattern = re.compile(r'^[A-Z]{3}([+-][0-9]*):([0-9]*)')
    tz_g = pattern.match(tz_str)
    tzh_int = int(tz_g.group(1))
    tzm_int = int(tz_g.group(2))
    tz_info = timezone(timedelta(hours=tzh_int, minutes=tzm_int))
    dtt = dt.replace(tzinfo=tz_info)
    dt_s = dtt.timestamp()
    print(dt_s, tzh_int, tzm_int)
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
