# -*- coding: utf-8 -*-

#
# author:zcy
# time:2019-02-21
# fuction:爬取豆瓣2016年度书单,直接从 json 中获取

import scrapy
from scrapy import Request

from ..items import AnnualListItem
from selenium import webdriver
import json
#from selenium import webdriver
#import selenium.webdriver.chrome.service as service


class DoubanbookSpider(scrapy.Spider):
    name = 'doubanBook-2018'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    
    
    def start_requests(self):
        
        base_url = 'https://book.douban.com/ithil_j/activity/book_annual2018/widget/%s'
        for i in range(41):
            url = base_url % i
            yield Request(url)
#        url = base_url % 1
#        yield Request(url)
            
            
    # 依次加载下一个页面，通过 url 的变化，直到最后一页
#    def parse_url(self, response):
#        pass
#    
    def parse(self, response):   
        body = json.loads(response.body)['res']
        
        # 挑选书单页
        if "Top" not in body['kind_cn']:
            return
        
        annuallist = AnnualListItem()
        # 提取书单名称
        listtitle = body['payload']['title']
 
        text = body['subjects']
        for i in range(len(text)):
            annuallist['listname'] = listtitle
            annuallist['bookname'] = text[i]['title']
            annuallist['score'] = text[i]['rating']
            annuallist['index'] = i
            annuallist['link'] = text[i]['url']
            
            yield annuallist
            
            
        
        
    

#############################################
#        #2018 页面分析
#        listname= response.css('h1 div::text').extract_first()
#        # 提取第一本书                      
#        yield self.firstBook(response)
#        
#        # 提取第二至十本书        
#        le = LinkExtractor(restrict_css='li._111mb')
#        links = le.extract_links(response)
#        if len(links) > 0: 
#            for i in range(9):
#                yield self.otherBook(listname,links[i])
#        
#      
#    # 提取第一本书的链接和书名    
#    def firstBook(self, response):
#        annuallist = AnnualListItem()
#        annuallist['listname'] = response.css('h1 div::text').extract_first()
#        le = LinkExtractor(restrict_css='div._2mn2i')
#        books = le.extract_links(response)   
#        if len(books) > 0: 
#            annuallist['bookname'] =  books[0].text    
#            annuallist['link'] = books[0].url
#            annuallist['score'] = response.css('div._2YEJY::text').extract_first()
#            return  annuallist
#    
#    # 提取第 2-10 本书的链接和书名
#    def otherBook(self, listname, link):
#                
#        annuallist = AnnualListItem()
#        
#        # 去掉字符串中的数字
#        remove_digits = str.maketrans('', '', digits)
#  
#        annuallist['listname'] = listname       
#        annuallist['bookname'] = link.text.translate(remove_digits).rstrip('.')
#        annuallist['link'] = link.url
#        annuallist['score'] = link.text[-3:]
#        return  annuallist
        
