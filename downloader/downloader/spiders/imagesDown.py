# -*- coding: utf-8 -*-
import scrapy


class ImagesdownSpider(scrapy.Spider):
    name = 'imagesDown'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def parse(self, response):
        pass
