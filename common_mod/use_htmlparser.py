#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/8 13:43
@Author : chao
@File   : use_htmlparser.py
'''
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    # 定义一个子类，继承HTMLParser
    # 该子类中定义的方法都是重写的父类中已有的方法

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser() # 创建解析器的实例
# 调用feed方法
parser.feed(
    '''
    <html>
    <head></head>
    <body>
    <!-- test html parser -->
        <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END
    </p>
    </body>
    </html>
    '''
)

