# -*- coding: utf-8 -*-

#
# author:zcy
# time:2019-02-25
# fuction:从数据库中各个榜单中的链接去豆瓣爬取书籍的信息种类

import scrapy
from scrapy import Request
from pymongo import MongoClient

from scrapy.selector import Selector


class bookinfoSpider(scrapy.Spider):
    name = 'bookinfo'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/subject/26681991/', 'https://book.douban.com/subject/30131339/']
 
    
    def start_requests(self):
        
        # 连接数据库
        db_uri = 'mongodb://localhost:27017'
        db_name = 'zcy_scrapy_data'
        
    
        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]
        
        collection_name  = "doubanBook-%s"
        for i in range(3):
            collection = self.db[collection_name % (2016+i)]
            
            # 读取数据
            books = collection.find({}, { 'bookname':1, 'link':1})
            
            for book in books:
                book_name = book['bookname']
                book_link = book['link']
                base_url = book_link
                print(base_url)
                yield Request(base_url)
                
            
                

    
    def parse(self, response):  
        print(response.url)
      
        # 提取所有 2015 年度榜单的 CSS 样式
        book_name = response.css('div#wrapper h1 span::text')
        book_infos = response.css('div#wrapper div#content div#info ').extract()
        
        aaa = str(book_infos).split("<br>")                          
        for info in aaa:
            
            # 去掉乱七八糟的一些空白符
            index = info.find('<span class="pl">') 
            if index != -1:
                info = info[index:]
            
            
            info_1 = Selector(text=info).css('*::text').extract()
            info_2 = [x for x in info_1 if '\\n' not in x] 
            if info_2:
                yield {'name':info_2[0].lstrip()}

                
                

            
      
        
        
        
        