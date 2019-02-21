# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:20:50 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import time

class ProxyLanternSpider(scrapy.Spider):
    name = 'ProxyLantern'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['https://free-proxy-list.net']
     
    def start_requests(self):
        # 请求第一页
        yield Request('https://free-proxy-list.net/')
      
    def parse(self, response):
        
        for sel in response.css('div.table-responsive tr'):
            # 提取代理的 IP、port、scheme（http or https）
            ip = sel.css('td:nth-child(1)::text').extract_first()
            port = sel.css('td:nth-child(2)::text').extract_first()
           
           
            if sel.css('td:nth-child(7)::text').extract_first() == 'yes':
                scheme = "https"
            else:
                continue

            
            # 使用爬取到的代理再次发送请求到 http(s)://httpbin.org/ip, 验证代理是否可用
            url = '%s://httpbin.org/ip' % scheme
            proxy = '%s://%s:%s' % (scheme, ip, port)
            
            meta = {
                'proxy': proxy,
                'dont_retry': True,
                'download_timeout':10,
                
                # 以下两个字段是传递给 check_available 方法的信息，方便检测
                '_proxy_scheme': scheme,
                '_proxy_ip': ip,
                
            }
            
            yield Request(url, callback=self.check_available, meta=meta, dont_filter=True)
            
    def check_available(self, response):
        proxy_ip = response.meta['_proxy_ip']
        
        # 判断代理是否具有隐藏 ip 的功能
        if proxy_ip == json.loads(response.text)['origin']:
            yield {
                'proxy_scheme': response.meta['_proxy_scheme'],
                'proxy': response.meta['proxy'],
                'time':time.localtime()
            }
            
        if response.meta['proxy'] == "https://134.249.142.70:47204" or \
        response.meta['proxy'] == "https://198.27.67.35:3128" or \
        response.meta['proxy'] == "https://123.201.19.116:44978" or \
        response.meta['proxy'] == "https://46.165.49.41:47712" :
            yield {
                'proxy_scheme': response.meta['_proxy_scheme'],
                'proxy': response.meta['proxy'],
            }
            

