# -*- coding: utf-8 -*-

#
# author:zcy
# time:2019-02-21
# fuction:爬取豆瓣2015年度书单

import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from ..items import AnnualBookItem
from ..items import AnnualListItem
from scrapy.linkextractors import LinkExtractor
from string import digits

#lua_script = """
#function main(splash)
#    splash:go(splash.args.url)
#    splash:wait(0.5)
#    splash:runjs("document.getElementsByClassName('down-btn')[0].click()")
#    return splash:html()
#end
#"""
#    splash:wait(0.5)
#    splash:runjs("document.getElementsByClassName('down-btn')[0].scrollIntoView(true)")
#
class DoubanbookSpider(scrapy.Spider):
    name = 'doubanBook-2015'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    
    
    def start_requests(self):
        #请求第一页，
        base_url = 'https://book.douban.com/annual/2015'
        yield Request(base_url)
#        yield SplashRequest(base_url, endpoint='execute', args={'lua_source':lua_script}, cache_args=['lua_source'], dont_filter=True)
        
    # 依次加载下一个页面，通过 url 的变化，直到最后一页
    def parse_url(self, response):
        pass
    
    def parse(self, response):       
        
        annuallist = AnnualListItem()
        
        # 提取所有 2015 年度榜单的 CSS 样式
        lists = response.css('div.section.top-10-widget')
        
        # 每次循环处理一个榜单
        for l in lists:
            
            # 提取榜单名称
            lname= l.css('tr.top-column div::text').extract()              
            a = [x for x in lname if '\n' not in x]
            b = ''.join(a)
            annuallist['listname'] = b
            
            # 提取该榜单内的书名和评分
            books = l.css('div.subjects-section a')
            for index,book in enumerate(books):              
                d = book.css('p::text').extract()
                e = [x for x in d if '\n' not in x]                
                annuallist['bookname'] = e[0]
                annuallist['score'] = e[1]
                annuallist['index'] = index
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
        
