# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#在这里导入 Item，提示 “ValueError: attempted relative import beyond top-level package”
#from scrapy import Item
#from ..items import ProxyExampleItem
from pymongo import MongoClient

# 暂时没想好
class BookPipeline(object):
    def process_item(self, item, spider):
        return item

# MongoDB 数据库插件
class MongoDBPipeline(object):
    
    # 打开数据库
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI', '')
        db_name = spider.settings.get('MONGODB_NAME', '')
        
        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]
        
    # 关闭数据库
    def close_spider(self, spider):
        self.db_client.close()
    
    # 存入数据库
    def process_item(self, item, spider):
        self.insert_db(item, spider)
        return item
    
    # 插入数据
    def insert_db(self, item, spider):
#        if isinstance(item, Item):          #此处
        item = dict(item)
        
            
        collection = self.db[spider.name]
        collection.insert_one(item)
          
    