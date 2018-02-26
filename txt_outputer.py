#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:51:23 2017 

@author: panchencheng
""" 

class TxtOutputer():
    
    def __init__(self):
        self.datas = []
        
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
       # ascii 
    def output_txt(self):
        with open("output.txt",'w') as fout: #建立文件输出对象
        
            for data in self.datas:
                fout.write("URL链接：")
                fout.write(data['url'])
                fout.write("\r\n问题标题：")
                fout.write(data['QuestionHeader'].encode('UTF-8'))
                fout.write("\r\n问题描述：")
                fout.write(data['RichText'].encode('UTF-8'))
                fout.write("\r\n被浏览次数：")
                fout.write(data['BrowseNumber'].encode('UTF-8'))
                fout.write("\r\n关注人数：")
                fout.write(data['FollowersNumber'].encode('UTF-8'))
                fout.write("\r\n答案：\r\n")
                fout.write(data['Answer'].encode('UTF-8'))
                fout.write("\r\n答案作者：")
                fout.write(data['Writer'].encode('UTF-8'))
                fout.write("\r\n")
                fout.write(data['Good'].encode('UTF-8'))
                fout.write("\r\n答案的评论：\r\n")
                fout.write(data['CommentList'].encode('UTF-8'))
                fout.write("\r\n")
                fout.write("\r\n")
                fout.write("\r\n")
                fout.write("\r\n")
        #闭合标签
            fout.close()