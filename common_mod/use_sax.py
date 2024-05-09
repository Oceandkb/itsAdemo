#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/8 09:05
@Author : chao
@File   : use_sax.py
'''

# 操作XML有两种方法：DOM和SAX
# DOM将整个XML读入内存，解析为树，内存占用大，解析慢，优点是可以任意遍历树的节点
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件
# SAX是优先使用的方法
# 通常关心的事件是start_element, end_element, char_data、

# 导入xml.parsers.expat中的一个ParseCreat类，创建XML解析器
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        # 处理xml中的开始标签事件
        # name参数表示元素名称，attrs参数是一个字典，表示元素的属性和值
        print('sax: start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        # 处理xml中的结束标签事件
        # name就是元素的名称
        print('sax: end_element: %s' % name)

    def char_data(self, text):
        # 处理xml中的文本内容事件
        # text表示元素的文本内容
        print('sax: char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler() # 创建一个实例对象，作为事件处理的程序
parser = ParserCreate() # 创建一个ParserCreate的实例，用于创建XML解析器
parser.StartElementHandler = handler.start_element
# 将parser实例中的StartElementHandler属性设置为handler对应的方法
# 将事件处理程序和xml解析器关联起来
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml) # 解析器调用Parse方法，解析xml

# 整个思路就是自己创建一个包含打印各种事件方法的类
# 然后利用ParserCreate这个类去创建解析器
# 将自己定义的打印事件的方法赋值给解析器对应的属性
# 这样在解析器解析xml时，如果遇到了start_element就会去调handler.start_element方法
# 对元素的开始标签进行处理


# 如何生成XML
import xml.sax.saxutils
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(xml.sax.saxutils.escape('some & data'))
L.append(r'</root>')
print(''.join(L))

# 练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
from urllib import request

# 思路
# 通过urllib获取天气预报网页的xml数据
def parseXml(xml_str):
    print(xml_str)
    return