# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
import json
import pytesseract
from PIL import Image
from io import BytesIO
from scrapy.log import logger

class KuwoLoginSpider(scrapy.Spider):
    name = 'kuwo_login'
    allowed_domains = ['hrb.lianjia.com']
    start_urls = ['https://hrb.lianjia.com/']

    def parse(self, response):
        pass
    
    # 链家网页的登录页面
    login_url = 'https://upassport.lianjia.com/dist/js/passport.js'
    user = '18324519124'
    password = 'xiaoXIAO585lj'
        
    def start_requests(self):
        yield Request(self.start_urls, callback=self.login, dont_filter=True )
        
    def login(self, response):
        # 该方法既是登录页面的解析函数，也是下载验证码图片的响应处理函数
        # 如果 response.meta['login_response'] 存在，当前 response 为严重图片，否则当前 response 为登录页面的响应
        login_response = response.meta.get('login_response')
        
        if not login_response:
            # step 1:
            # 此时 response 为登录页面的响应，从中提取验证码图片的 url 
            captchaUrl = response.css('label.field.prepend-icon img::attr').extract_first()
            
            captchaUrl = response.urljoin(captchaUrl)
            # 构造 Request 时，将当前 response 保存到 meta 字典中
            yield Request(captchaUrl, callback=self.login,meta={'login_response':response},dont_filter=True)
            
        else:
            # step 2:
            # 此时 response 为验证码图片的响应，response.body 是图片的二进制数据
            formdata = {
                'email' :self.user,
                'pass':self.password,
                # 使用 OCR识别
                'code':self.get_captcha_by_OCR(response.body),
            }
            yield FormRequest.form_response(login_response, callback=self.parse_login,formdata=formdata, dont_filter=True)
            
    def parse_login(self, response):
        info = json.loads(response.text)
        if info['error'] == '0':
            logger.info('登录成功')
            return super().start_requests()
        logger.info('登录失败')
        return self.start_requests()
    
    def get_captcha_by_OCR(self,data):
        # OCR 识别
        img = Image.open(BytesIO(data))
        img = img.convert('L')
        captcha = pytesseract.image_to_string(img)
        img.close()
        return captcha