#! env: python3
#! -*- coding:utf-8 -*-
import Crawler

class torlock():
    def __init__(self,url="https://torlock.com"):
        self.url = url;
        self.inside_list = set()
        self.outside_list = set()
        self.tor_list = set()
        self.source_list = set()
        self.pages = {}
        self.spider = Crawler.crawler(self.url)
        self.basepage = self.spider.basePage
        
    def crawl(self,url):
        if (url in self.inside_list):
            return 0
        print(url) 
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
        self.inside_list.add(url)
        self.outside_list = self.outside_list.union(outside)
        self.tor_list = self.tor_list.union(tor)
        self.source_list = self.source_list.union(source)
        for url in inside.difference(self.inside_list):
            self.crawl(url)
            if len(self.tor_list) > 100:
                break
        #for url in outside.difference(self.outside_list):
        #    self.crawl(url)

    def save_tor(self,filename = "tor.txt"):
        fp = open(filename,'w')
        for tor in self.tor_list:
            fp.write(tor + '\n')
        fp.close()
    def save_source(self, filename = "source.txt"):
        fp = open(filename,'w')
        for source in self.source_list:
            fp.write(source + '\n')
        fp.close()

