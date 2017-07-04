#i! env: python3
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
        headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87  Safari/537.36'}
        self.session.headers = headers
    
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
            if url.startswith('/') or url.startswith('./'): 
                if (url.startswith('./')):
                    url = url[1:]
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
                    tor_list.add(url+ ": " + name)
                elif re.match(sourcePattern,url):
                    source_list.add(url)
                else:
                    inside_url_list.add(url)
            elif url.startswith('http'):
                url = url.split("://")[1]
                url = url.replace('?','/')
                url = url.split('/')[0]
                if len(re.findall(r'\.',url)) > 1:
                    url = re.search(r'.*\.+(.*\..*)',url).group(1)
                else:
                    pass
                if url.startswith('https'):
                    url = 'https://' + url
                else:
                    url = 'http://' + url
                outside_url_list.add(url)
        for node in page.select('[src]'):
            url = node.get('src')
            if url.startswith('/') or url.startswith('./'): 
                if (url.startswith('./')):
                    url = url[1:]
                if url.endswith('.torrent'):
                    name = page.find('title').text
                    tor_list.add(self.url + url + ": " + name)
                elif re.match(sourcePattern,url):
                    source_list.add(self.url + url)
                else:
                    inside_url_list.add(self.url + url)
            elif not url.startswith('http'): 
                if url.endswith('.torrent'):
                    name = page.find('title').text
                    tor_list.add(self.url + '/' + url + ": " + name)
                elif re.match(sourcePattern,url):
                    source_list.add(self.url + '/'  + url)
                else:
                    inside_url_list.add(self.url + '/'  + url)
            elif url.startswith('http'): 
                if url.endswith('.torrent'):
                    name = page.find('title').text
                    tor_list.add(url + ": " + name)
                elif re.match(sourcePattern,url):
                    source_list.add(url)
                else:
                    inside_url_list.add(url)
            

        return inside_url_list, outside_url_list, tor_list, source_list



            


            

         


        



