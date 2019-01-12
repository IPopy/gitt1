# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:05:14 2019

@author: zcy

@error:
    花费一个多小时的时间调试，详细错误见 error.txt
"""
import scrapy
from scrapy.http import Request, FormRequest

class LoginsSpider(scrapy.Spider):
    name = 'logins'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile']

    def parse(self, response):
        keys = response.css('table label::text').re('(.+):')
        values = response.css('table td.w2p_fw::text').extract()
        
        yield dict(zip(keys,values))
        
        
    # -----------------登录---------------------
    login_url = 'http://example.webscraping.com/places/default/user/login'
    
    def start_requests(self):
        yield Request(self.login_url, callback=self.login)
        
    def login(self, response):
        # 登录页面的解析函数，构造 FormRequest 对象提交表单
        fd = {'email' : 'spzhangcy@gmail.com', 'password' : '123456'}
        yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)
        
    def parse_login(self, response):
        # 登录成功后，继续爬取 start_url 中的页面
        if 'Welcome' in response.text:         
            yield from super().start_requests() # 