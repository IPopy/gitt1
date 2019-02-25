# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from collections import defaultdict
import json
import random
from scrapy.exceptions import NotConfigured

from scrapy.http import HtmlResponse
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.common.exceptions import TimeoutException
from AnnualBook.configs import CHROME_DRIVER_PATH
import time

# 随机选择代理文件中的一个代理
class RandomHttpProxyMiddleware(HttpProxyMiddleware):
    def __init__(self, auth_encoding='latin-1', proxy_list_file=None):
        if not proxy_list_file:
            raise NotConfigured
            
        self.auth_encoding = auth_encoding
        self.proxies = defaultdict(list)
        
        # 从 json 文件中读取代理服务器的信息， 填入 self.proxies
        with open(proxy_list_file) as f:
            proxy_list = json.load(f)
            for proxy in proxy_list:
                scheme = proxy['proxy_scheme']
                url = proxy['proxy']
                self.proxies[scheme].append(self._get_proxy(url, scheme))
             
    @classmethod
    def from_crawler(cls, crawler):
        # 从配置文件中读取用户验证信息的编码
        auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'latin-1')
        # 从配置文件中读取代理服务器列表文件的路径
        proxy_list_file = crawler.settings.get('HTTPPROXY_PROXY_LIST_FILE')
        return cls(auth_encoding, proxy_list_file)
    
    def _set_proxy(self, request, scheme):
        # 随机选择一个代理

        creds, proxy = random.choice(self.proxies[scheme])
        request.meta['proxy'] = proxy
        if creds :
            request.headers['Proxy-Authorization'] = b'Basic' + creds



class ChromeDownloaderMiddleware(object):
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
#        options.add_argument('--disable-gpu')
        chromedriver_path = CHROME_DRIVER_PATH 
        self.driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver_path)
    
    def __del__(self):
        self.driver.close()
        
    
    def process_request(self, request, spider):
    
        try:
            print('Chrome driver begin...')
            self.driver.get(request.url)        # 获取网页链接内容  
            time.sleep(20)       
            print('cccccccccccccccccccccccccccccccccccc')
            print('cccccccccccccccccccccccccccccccccccc')
            print('cccccccccccccccccccccccccccccccccccc')             
            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',status=200) # 返回HTML数据
        except TimeoutException:
            print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
            print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
            print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
            return HtmlResponse(url=request.url, request=request, encoding='utf-8', status=500)
        finally:
            print('Chrome driver end...')
    