# -*- coding: utf-8 -*-
import scrapy
import json


class ImagesdownSpider(scrapy.Spider):
    BASE_URL = 'https://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    start_index = 30
    
    name = 'imagesDown'
    allowed_domains = ['image.so.com']
    start_urls = [BASE_URL % 0]

    
    # 限制最大下载数量，防止磁盘用量过大
    MAX_DOWNLOAD_NUM = 1000
    
    def parse(self, response):
        # 使用 json 模块解析响应结果
        infos = json.loads(response.body.decode('utf-8'))
        # 提取所有图片下载 url 到一个列表，赋值给 item 的 ‘image_urls’字段
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        # 上面的一行代码只给 'image_url' 赋值了，没有给 'images' 赋值，交给imagespipeline处理。
        
        # 如 count 字段大于 0， 并且下载数量不足 MAX_DOWNLOAD_NUM, 继续获取图片
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index, callback=self.parse)