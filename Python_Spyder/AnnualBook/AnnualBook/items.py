# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

# 图书表 
class AnnualBookItem(scrapy.Item):
    name = Field()              #书名
    author = Field()            #作者
    date = Field()              #出版日期
    ISBN = Field()              #ISBN
    page = Field()              #页数
    formerName = Field()        #原名
    translator = Field()        #译者
    price = Field()             #价格
    doubanScore = Field()       #豆瓣分数
    doubanManNum = Field()      #豆瓣评分人数
    
    
# 榜单表
class AnnualListItem(scrapy.Item):
    listname = Field()          #榜单名
    bookname = Field()          #书名
    link = Field()              #链接
    score = Field()             #豆瓣评分
