#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:50:14 2017

@author: panchencheng
"""
import urllib2
import cookielib

class HtmlDownloader():
    
    def download(self, url):
        if url is None:
            return None
        
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()