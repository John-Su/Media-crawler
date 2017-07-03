#! env: python3
#! -*- coding:utf-8 -*-
import Crawler
import os
import time
import codecs
import re
timeFormat = '%Y-%m-%d %H:%M:%S'

class webSite():
    def __init__(self,url="https://torlock.com"):
        self.url = url;
        self.inside_list = set()
        self.outside_list = set()
        self.tor_list = set()
        self.source_list = set()
        self.pages = {}
        url = url.split("://")
        rootPath = url[1] if len(url) > 1 else url[0]
        rootPath = rootPath.split('/')[0]
        if len(re.findall(r'\.',rootPath)) > 1:
       	        self.rootPath ='output/' + re.search(r'.*\.+(.*\..*)',rootPath).group(1)
        else: 
	        self.rootPath ='output/' +rootPath
        self.spider = Crawler.crawler(self.url,self.rootPath)
        self.basepage = self.spider.basePage
        try:
                os.mkdir(self.rootPath)
        except Exception:
                pass


        
    def crawl(self,url):
        if (url in self.inside_list):
            return 0
        self.pages[url] = {}
        inside, outside, tor, source = self.spider.analyze_page(self.spider.crawl_page(url))
        self.pages[url]['inside'] = inside
        self.pages[url]['outside'] = outside
        self.pages[url]['tor'] = tor
        self.pages[url]['source'] = source
        self.pages[url]['inside_count'] = len(inside)
        self.pages[url]['outside_count'] = len(outside)
        self.pages[url]['tor_count'] = len(tor)
        self.pages[url]['source_count'] = len(source)
        # add the url in to the crawled list
        self.inside_list.add(url)
        self.outside_list = self.outside_list.union(outside)
        self.tor_list = self.tor_list.union(tor)
        self.source_list = self.source_list.union(source)
        if len(self.tor_list) > 1 or len(self.source_list) > 1:
       	    return 0   
        for url in inside.difference(self.inside_list):
            self.crawl(url)
            if len(self.tor_list) > 1 or len(self.source_list) > 1:
       	        break
        return 0
        #for url in outside.difference(self.outside_list):
        #    self.crawl(url)

    def save_tor(self,filename = "/tor.txt"):
        fp = codecs.open(self.rootPath + filename,'w','utf-8')
        fp.write('\n')
        for tor in self.tor_list:
            fp.write('['+time.strftime(timeFormat,time.localtime(time.time()))+'] ')
            fp.write(tor + '\n')
        fp.close()

    def save_source(self, filename = "/source.txt"):
        fp = codecs.open(self.rootPath + filename,'w','utf-8')
        fp.write('\n')
        for source in self.source_list:
            fp.write('['+time.strftime(timeFormat,time.localtime(time.time()))+'] ')
            fp.write(source + '\n')
        fp.close()

    def save_outSide(self,filename = "/outside.txt"):
        fp = codecs.open(self.rootPath + filename,'w','utf-8')
        fp.write('\n')
        for site in self.outside_list:
            fp.write('['+time.strftime(timeFormat,time.localtime(time.time()))+'] ')
            fp.write(site + '\n')
        fp.close()

    def save_inSide(self,filename = "/inside.txt"):
        fp = codecs.open(self.rootPath + filename,'w','utf-8')
        fp.write('\n')
        for site in self.inside_list:
            fp.write('['+time.strftime(timeFormat,time.localtime(time.time()))+'] ')
            fp.write(site + '\n')
        fp.close()

