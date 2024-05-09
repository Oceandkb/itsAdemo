#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/9 10:32
@Author : chao
@File   : use_psutil.py
'''

import psutil

# 获取cpu逻辑数量
cc = psutil.cpu_count()
print(cc)
# 获取cpu物理数量
ccc = psutil.cpu_count(logical=False)
print(ccc)

# 统计cpu的用户/系统/空闲时间
print(psutil.cpu_times())
# result：
# scputimes(user=1127518.07, nice=0.0, system=571405.16, idle=5299765.42)
# user：cpu在用户模式下花费的时间（就是用户主动用的）
# system：cpu在系统模式下花费的时间（系统内置的）
# idle： cpu处于空闲状态的时间



# 实现linux中的top命令，cpu的使用率
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
# 和free -m的效果一样
print(psutil.virtual_memory()) # 物理内存
# svmem(total=17179869184, available=4086874112, percent=76.2, used=6252789760, free=49971200,
# active=4052877312, inactive=4036149248, wired=2199912448)

print(psutil.swap_memory()) # 交换内存信息

# 获取磁盘信息
print(psutil.disk_partitions()) # 磁盘分区信息
print(psutil.disk_usage('/')) # 磁盘使用情况
print(psutil.disk_io_counters()) # 磁盘IO

# 获取网络信息
print(psutil.net_io_counters()) # 网络读写的字节/包的个数
print(psutil.net_if_addrs()) # 获取网络接口信息
print(psutil.net_if_stats()) # 获取网络接口状态
# print(psutil.net_connections()) # 获取网络链接信息
# 这个有可能会报错，因为需要root权限
print(psutil.pids()) # 获取所有进程号

p = psutil.Process(317)
print(p.name())
