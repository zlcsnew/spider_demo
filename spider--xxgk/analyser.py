#!-*- coding:utf-8 -*-
import re
pat1='''<div class="gksq"><h1>联系我们</h1>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?</div>''';  # type: unicode
pat2='''<div class="gksq tsjd"><h1>监督投诉</h1>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?<p>(.*?)</p>\s*?</div>''';
def findall(data):
    global pat1
    global pat2
    result1=re.compile(pat1).findall(data);
    result2=re.compile(pat2).findall(data);
    return result1[0],result2[0]