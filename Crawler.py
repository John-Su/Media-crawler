#! env: python3
#! -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

class crawler():
    
    def __init__(self,url=''):
        self.url = url;
        self.session = requests.session()
        self.basePage = self.crawl_page(self.url)
    
    def crawl_page(self,url):
        r = self.session.get(url)
        return BeautifulSoup(r.text,'lxml')

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
                    name = page.find('dd').text
                    tor_list.add(self.url + url + ": " + name)
                elif not (url.endswith('.html') or url.endswith('.htm')):
                    source_list.add(self.url + url)
                else:
                    inside_url_list.add(self.url + url)
            elif url.startswith(self.url):
                if url.endswith('.torrent'):
                    name = page.find('dd').text
                    print (url+ ": " + name)
                    tor_list.add(url+ ": " + name)
                elif not (url.endswith('.html') or url.endswith('.htm')):
                    source_list.add(url)
                else:
                    inside_url_list.add(url)
            elif url.startswith('http'):
                outside_url_list.add(url)
        return inside_url_list, outside_url_list, tor_list, source_list



            


            

         


        



