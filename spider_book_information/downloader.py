#!-*- coding:utf-8 -*-
import urllib2
import analyzer
import config
import zlib
import time
def getPage(url_list,number):
    fail_list=url_list;
    result_dict=dict();
    for url in fail_list:
        urlhash=hash(url);
        if result_dict.has_key(urlhash):
            print("url redo!")
            continue
        result_dict[urlhash]=[]
        for page in range(1,number+1):
            if page==1:
                data=getHTML(url);
            else:
                data=getHTML(url,page);
            if data==None:
                continue
            yield  urlhash,data
    yield  None,None
            #informations=analyzer.get_informations(data)
            #result_dict[urlhash]=result_dict[urlhash]+informations;

def getHTML(url,number=1):
    if number!=1:
        url=url+'&Page=%s'%(number);
    print(url)
    opener = urllib2.build_opener();
    opener.addheaders = [config.http_header];
    try:
        response = opener.open(url);
        data = response.read();
        gzipped = response.headers.get('Content-Encoding');
        if gzipped:
            print("decompressing")
            data = zlib.decompress(data, 16 + zlib.MAX_WBITS);
        else:
            pass
        data = data.decode('utf-8');
        time.sleep(10)
        return data
    except urllib2.HTTPError:
        print(url, urllib2.HTTPError.code, urllib2.HTTPError.reason, "try again")
        return None
    except urllib2.URLError:
        print(url, "in URLError,abort")
        return None
