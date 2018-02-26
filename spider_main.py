#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:46:43 2017

@author: panchencheng
爬虫总调度程序
"""
import sys
stdo = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout= stdo

import urllib

import url_manager, html_downloader, html_parser, txt_outputer

class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = txt_outputer.TxtOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                
                print "craw %d : %s"%(count, new_url)
                
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 10:
                    break;
                
                count = count+1
            except Exception,e:
                print e
                print 'craw failed' #异常处理
                
        self.outputer.output_txt()
        

if __name__== '__main__':
    f= open("key_word.txt","r")
    key_word= f.read()
    key_word = urllib.quote(key_word)
    root_url = "https://www.zhihu.com/search?q="+key_word+"&type=content"
    #爬虫入口URL
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) #启动爬虫
    
    

