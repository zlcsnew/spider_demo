#-*-coding:utf-8-*-
import urllib2
import config
import sys
import zlib
def getPages(url_list):
    success_list = [];
    fail_list = url_list;
    result_dict = dict();
    type = sys.getfilesystemencoding()
    for i in range(0, config.retry_times):
        now_index = 0;
        downloader_size = len(fail_list);
        tmp_fail = [];
        for url in fail_list:
            opener = urllib2.build_opener();
            opener.addheaders = [config.http_header];
            try:
                response= opener.open(url);
                data=response.read();
                gzipped = response.headers.get('Content-Encoding');
                if gzipped:
                    print("decompressing")
                    data= zlib.decompress(data, 16 + zlib.MAX_WBITS);
                else:
                    pass
                data=data.decode('utf-8').encode('utf-8');
                result_dict[hash(url)] = data;
                f=open('/home/spark/mobile_internet/spider/test.data','w')
                f.write(data)
                f.close()
            except urllib2.HTTPError:
                print(url, urllib2.HTTPError.code, urllib2.HTTPError.reason, "try again")
                tmp_fail.append(url);
            except urllib2.URLError:
                print(url, "in URLError,abort")
        fail_list = tmp_fail;
    return result_dict
