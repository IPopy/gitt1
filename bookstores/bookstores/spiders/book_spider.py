# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:22:24 2019

@author: Administrator
"""

import scrapy
from ..items import BookstoresItem
from scrapy.linkextractors import LinkExtractor

class BooksSpider(scrapy.Spider):
    # 每个爬虫的唯一标识
    name = "books"
    
    # 定义爬虫爬取的起始点，可为多个
    start_urls = ['http://books.toscrape.com/']
    
    def parse(self, response):
        for sel in response.css('article.product_pod'):
            book = BookstoresItem()
            book['name'] = sel.xpath('./h3/a/@title').extract_first()
            book['price'] = sel.css('p.price_color::text').extract_first()
            yield book
            
        # 提取链接
#        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
#        if next_url:
#            next_url = response.urljoin(next_url)
#            yield scrapy.Request(next_url,callback=self.parse)
        le = LinkExtractor(restrict_css='ul.pager li.next' ) 
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url,callback=self.parse)