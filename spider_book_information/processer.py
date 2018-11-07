#!-*- coding:utf-8 -*-
import database_tool
import downloader
import analyzer
import config
import sys
def getBookInformation(url_list,number):
    database_tool.init();
    #for url in url_list:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    for urlhash,content_data in downloader.getPage(url_list,number):
            if urlhash == None:
                break;
            content_list=analyzer.get_informations(content_data);
            i=0;
            for item in content_list:
                sub_url=item[0];
                subpage=downloader.getHTML(config.url_base+sub_url,1);
                outcome=analyzer.get_time(subpage);
                outcome_tuple=(outcome,)
                content_list[i]=content_list[i][1:4]+outcome_tuple
                i=i+1;
            database_tool.insert_item(content_list)
            for content in content_list:
                print(content[0].decode(),content[1].decode(),content[2].decode(),content[3].encode())

