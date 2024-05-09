#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time   : 2024/5/8 14:11
@Author : chao
@File   : test_htmlparser.py
'''
# HTMLParser作业
# 找一个网页
# 例如https://www.python.org/events/python-events/，用浏览器查看源码并复制
# 然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
# 先定一个子类，继承HTMLParser，目的是要重写父类中的方法
# 用重写后的方法解析HTML中的事件、名称和地点等信息
class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.parse_data = '' # 设置一个空的标志位
        self.info = []

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.parse_data = 'name'

        if tag == 'time':
            self.parse_data = 'time'

        if ('class', 'say-no-more') in attrs:
            self.parse_data = 'year'

        if ('class', 'event-location') in attrs:
            self.parse_data = 'location'

    def handle_endtag(self, tag):
        # 在标签结束时，清空标志位
        # 为了在解析下一行html语句时时空的
        self.parse_data = ''

    def handle_data(self, data):
        if self.parse_data == 'name':
            self.info.append(f'会议名称:{data}')

        if self.parse_data == 'time':
            self.info.append(f'会议时间:{data}')

        if self.parse_data == 'year':
            self.info.append(f'会议年份: {data}')

        if self.parse_data == 'location':
            self.info.append(f'会议地点: {data}')

data = '''
      <li>
                        <h3 class="event-title"><a href="/events/python-events/1508/">PyCon US 2024</a></h3>
                        <p>
                            
                            
<time datetime="2024-05-15T00:00:00+00:00">15 May &ndash; 23 May <span class="say-no-more"> 2024</span></time>

                            

                            
                            <span class="event-location">Pittsburgh, Pennsylvania, USA</span>
                            
                        </p>
'''
parser = MyHTMLParser()
parser.feed(data)
for s in parser.info:
    print(s)