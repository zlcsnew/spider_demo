#!-*- coding:utf-8 -*-
import re
pat='''<dd>\s*?<span class="book_title">\s*?<a href="(.*?)" title="">(.*?)</a>\s*?</span>\s*?<span class="book_author">(.*?)</span>\s*?<span class="book_price"><b>(.*?)</b></span>\s*?</dd>''';
pat2=u'''<span>出版时间：(.*?)</span>'''
def get_informations(data):
    global pat
    result1 = re.compile(pat).findall(data);
    #print(result1)
    return result1;

def get_time(data):
    global pat2
    if data==None:
        return "0-0"
    result1 = re.compile(pat2).findall(data);
    return result1[0]
