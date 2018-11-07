#-*-coding:utf-8-*-
import analyser
import downloader
import config
import sys
def processor(url):
    reload(sys)
    sys.setdefaultencoding("utf-8")
    data_dict=downloader.getPages(url);
    for tmp_url in url:
        if tmp_url==None:
            break;
        print(tmp_url)
        tmp_key=hash(tmp_url);
        try:
            data2 = data_dict[tmp_key];
            result1, result2 = analyser.findall(data2);
            result = result1 + result2;
            for content in result:
                if config.content in content:
                    print content.encode("utf-8")
        except Exception:
            pass

processor(['http://www.ucas.ac.cn/XXGK'])


