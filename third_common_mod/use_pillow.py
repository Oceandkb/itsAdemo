#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/8 16:18
@Author : chao
@File   : use_pillow.py
'''
from PIL import Image, ImageFilter

# 打开一个当前路径中的图像
im = Image.open('test.JPG')
# 获得图像尺寸
w, h = im.size
print('The original width is %s and height is %s of the picture' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %s*%s' % (w//2, h//2))
# 将缩放后的图片保存为jpeg
im.save('thum.jpeg', 'jpeg') # fp代表保存文件的名称，format代表要保存的格式

# 对图像应用模糊滤镜
imm = Image.open('test.JPG')
im2 = imm.filter(ImageFilter.BLUR)
im2.save('blur.JPG', 'jpeg')

# PIL的ImageDraw还提供了一系列的画图方法
# 生成字母验证码图片
from PIL import ImageDraw, ImageFont
import random

# 随机字母
def randChar():
    return chr(random.randint(65, 90))

# 随机颜色
def randColor():
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))

# 随机颜色2
def randColor2():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


width = 60 * 4
height = 60
# Image.new方法创建一个新的图像，生成一个空白的图像
# 入参：颜色模式、图像尺寸、图像的初始颜色
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# Draw是图像绘制的方法
# 创建一个用于绘制的对象draw，入参是要绘制的图像
draw = ImageDraw.Draw(image)

# 填充每一个像素
# 通过一个嵌套的循环去遍历图像的每一个像素
for x in range(width):
    for y in range(height):
        # point方法用来绘制一个点
        # 入参是图像的像素位置和填充颜色
        draw.point((x, y), fill=randColor())

# 输出文字
# 使用循环的方式绘制文本
for t in range(4):
    # text方法绘制随机字符
    # 入参xy是文本的位置
    draw.text((60 * t + 10, 10), randChar(), font = font, fill=randColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')