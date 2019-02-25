# -*- coding: utf-8 -*-

#
# author:zcy
# time:2019-02-25
# fuction:从数据库中各个榜单中的链接去豆瓣爬取书籍信息

import scrapy
from scrapy import Request
from ..items import BookItem
from pymongo import MongoClient

from scrapy.selector import Selector


class bookSpider(scrapy.Spider):
    name = 'book'
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
#                book_name = book['bookname']
                book_link = book['link']
                base_url = book_link
                print(base_url)
                yield Request(base_url)
            break          
        self.db_client.close()       
            
                

    
    def parse(self, response):  
        book = BookItem()
        
        # 提取所有 2015 年度榜单的 CSS 样式
        book_name = response.css('div#wrapper h1 span::text').extract_first()
        book['name'] = book_name
        book_infos = response.css('div#wrapper div#content div#info ').extract()
        
        # 去掉 “\\n” 和前面的空白符 ,用 <br> 切分
        aaa = str(book_infos).split("<br>")  
        aaa = [x[x.find('<span class="pl">'):] for x in aaa]
        aaa = [x.replace('\\n','') for x in aaa]               
        for info in aaa:
            
            info_1 = Selector(text=info).css('*::text').extract()
            
            info_2 = [x.strip() for x in info_1 if '\\xa0' not in x]
            info_2 = [x for x in info_2 if '' != x and ':' != x]
            if len(info_2) > 1:
                
                info_name = info_2[0].lstrip()
                
                if "作者" in info_name:
                    book['author'] = info_2[1]
                elif "出版社" in info_name:
                    book['chubanshe'] = info_2[1]
                elif "出品方" in info_name:
                    book['chupinfang'] = info_2[1]
                elif "副标题" in info_name:
                    book['fubiaoti'] = info_2[1]
                elif "原作名" in info_name:
                    book['formername'] = info_2[1]
                elif "译者" in info_name:
                    book['translator'] = info_2[1]
                elif "出版年" in info_name:
                    book['date'] = info_2[1]
                elif "页数" in info_name:
                    book['page'] = info_2[1]
                elif "定价" in info_name:
                    book['price'] = info_2[1]
                elif "装帧" in info_name:
                    book['zhuangzhen'] = info_2[1]
                elif "ISBN" in info_name:
                    book['ISBN'] = info_2[1]
                elif "丛书" in info_name:
                    book['congshu'] = info_2[1]
          
        yield book
                
#    name = Field()              #书名
#    author = Field()            #作者
#    date = Field()              #出版年
#    ISBN = Field()              #ISBN
#    page = Field()              #页数
#    formername = Field()        #原作名
#    translator = Field()        #译者
#    price = Field()             #定价
#    zhuangzhen = Field()        #装帧
#    fubiaoti = Field()          #副标题
#    chupinfang = Field()        #出品方
#    chubanshe = Field()         #出版社
#    doubanScore = Field()       #豆瓣分数
#    doubanManNum = Field()      #豆瓣评分人数          

            
      
        
        
        
        