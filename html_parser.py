#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:50:49 2017

@author: panchencheng
"""
from bs4 import BeautifulSoup

from selenium import webdriver
import time

class HtmlParser():

    
    def _get_new_urls(self, page_url, soup):
        
        new_urls = set()
        
        browser = webdriver.Firefox(executable_path = '/Users/panchencheng/Desktop/软件课设-潘晨城/zhihu_spider/geckodriver')
        browser.get(page_url)
        browser.maximize_window()
        browser.execute_script("window.scrollBy(0,100000)")
        time.sleep(1)
        links = browser.find_elements_by_xpath("//a[contains(@href,'question') and contains(@href,'answer')]")
        
        for link in links:
            new_url = link.get_attribute('href')
            new_urls.add(new_url)
            
        browser.close()
        return new_urls
    
    def _get_new_data(self, page_url, soup):#解析数据
        res_data = {}
        res_data['url'] = page_url
#问题标题
        QuestionHeader_node = soup.find('h1', class_ ="QuestionHeader-title")
        if QuestionHeader_node is None:
            return  
        res_data['QuestionHeader'] = QuestionHeader_node.get_text()
        
#问题说明        
        RichText_node = soup.find('span', class_ ="RichText")
        if RichText_node is None:
            return  
        res_data['RichText'] = RichText_node.get_text()

        [FollowersNumber_node, BrowseNumber_node ]= soup.find_all('strong', class_ ="NumberBoard-itemValue",limit=2)
#问题被浏览次数
        if BrowseNumber_node is None:
            return  
        res_data['BrowseNumber'] = BrowseNumber_node.get_text()
#问题关注人数
        if FollowersNumber_node is None:
            return  
        res_data['FollowersNumber'] = FollowersNumber_node.get_text()
#答案
        Answer_node = soup.find('span', class_ ="RichText CopyrightRichText-richText")
        if Answer_node is None:
            return  
        res_data['Answer'] = Answer_node.get_text()

#答案的作者
        Writer_node = soup.find('span', class_ ="UserLink AuthorInfo-name")
        if Writer_node is None:
            return  
        res_data['Writer'] = Writer_node.get_text()
#答案的评论
        browser = webdriver.Firefox(executable_path = '/Users/panchencheng/Desktop/软件课设-潘晨城/zhihu_spider/geckodriver') 
        browser.get(page_url)

        browser.maximize_window()  

        Btn = browser.find_element_by_xpath("//button[@class='Button ContentItem-action Button--plain Button--withIcon Button--withLabel']")
        Btn.click()
        time.sleep(1)
        if browser.find_element_by_class_name('CommentList') is None:
             browser.close()
        res_data['CommentList'] = browser.find_element_by_class_name('CommentList').text    
        browser.close()
        
#答案的点赞次数  
        Good_node = soup.find('button', class_ ="Button Button--plain")
        if Good_node is None:
            return  
        res_data['Good'] = Good_node.get_text()            
        return res_data
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8') #soup对象
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls, new_data
        