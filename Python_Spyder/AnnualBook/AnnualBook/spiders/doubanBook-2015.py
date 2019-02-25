# -*- coding: utf-8 -*-

#
# author:zcy
# time:2019-02-21
# fuction:爬取豆瓣2015年度书单

import scrapy

from ..items import AnnualListItem




class DoubanbookSpider(scrapy.Spider):
    name = 'doubanBook-2015'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/annual/2015']
 
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
#                annuallist['link'] = 
                yield annuallist 
                return 
        
        
        
    