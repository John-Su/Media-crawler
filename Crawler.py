#! env: python3
#! -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
sourcePattern = r'.*(\.jpg|\.png|.gif)$'

class crawler():
    
    def __init__(self,url='',rootPath = ''):
        self.url = url;
        self.session = requests.session()
        self.basePage = self.crawl_page(self.url)
        self.rootPath = rootPath
    
    def crawl_page(self,url):
        try:
            r = self.session.get(url, timeout = 10)
            return BeautifulSoup(r.text,'lxml')
        except Exception:
            return BeautifulSoup('','lxml')

    def analyze_page(self,page):
        inside_url_list = set()
        outside_url_list = set()
        tor_list = set()
        source_list = set()
        if (not page.select('[href]')):
            return inside_url_list, outside_url_list, tor_list, source_list
        for node in page.select('[href]'):
            url = node.get('href')
            if url.startswith('/'): 
                if url.endswith('.torrent'):
                    name = page.find('title').text
                    tor_list.add(self.url + url + ": " + name)
                elif re.match(sourcePattern,url):
                    source_list.add(self.url + url)
                else:
                    inside_url_list.add(self.url + url)
            elif self.rootPath in url:
                if url.endswith('.torrent'):
                    name = page.find('title').text
                    print (url+ ": " + name)
                    tor_list.add(url+ ": " + name)
                elif not (url.endswith('.html') or url.endswith('.htm')):
                    source_list.add(url)
                else:
                    inside_url_list.add(url)
            elif url.startswith('http'):
                outside_url_list.add(url)
        return inside_url_list, outside_url_list, tor_list, source_list



            


            

         


        



