# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import FilesItem
class FilesdownSpider(scrapy.Spider):
    name = 'filesDown'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        #提取所有example的url
        le = LinkExtractor(restrict_css='div.toctree-wrapper li.toctree-l2 a')        
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_code)
            
        
    def parse_code(self, response):
        #提取source code的url
#        le = LinkExtractor(restrict_css='div.bodywrapper p', allow='matplotlib.org/examples')
#        link = le.extract_links(response)
        le = LinkExtractor(restrict_css='a.reference.external')
        link = le.extract_links(response)
        
        file = FilesItem()
        file['file_urls'] = [link[0].url]
        return file
    
#    def parse(self, response):
#        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny='/index.html$')
#
# #       print len(le.extract_links(response))
#        for link in le.extract_links(response):
#            yield scrapy.Request(link.url, callback=self.parse_example)
#            break
#
#    def parse_code(self, response):
#        href = response.css('a.reference.external::attr(href)').extract_first()
#        url = response.urljoin(href)
#        example = FilesItem()
#        example['file_urls'] = [url]
#        return example
       
