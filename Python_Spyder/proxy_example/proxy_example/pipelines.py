# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Item
from pymongo import MongoClient

class ProxyExamplePipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI', '')
        db_name = spider.settings.get('MONGODB_DB_NAME', '')
        
        self.db_client = MongoClient('mongodb://localhost:27017')
        self.db = self.db_client[db_name]
        
    def close_spider(self, spider):
        self.db_client.close()
        
    def process_item(self, item, spider):
        self.insert_db(item, spider)
        return item
    
    def insert_db(self, item, spider):
        if isinstance(item, Item):
            item = dict(item)
            
        collection = self.db[spider.name]
            
        collection.insert_one(item)    
     