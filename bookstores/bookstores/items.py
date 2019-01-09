# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BookstoresItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    #authors = scrapy.Field(serializer=lambda x: '|'.join(x))

class BookItem(scrapy.Item):
    name = Field()              #书名
    price = Field()             #价格
    review_rating = Field()     #评价等级
    review_num = Field()        #评价数量
    upc = Field()               #产品编码
    stock = Field()             #库存数量