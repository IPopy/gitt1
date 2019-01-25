# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
import json
import pytesseract
from PIL import Image
from io import BytesIO
import logging
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import open_in_browser



# js
#  splash:runjs("document.getElementsByClassName('tologin')[1].click()")
# 手机验证码登录界面
lua_script = """
function main(splash)
    
    splash:wait(0.5)
    splash:go("https://www.baidu.com")
    splash:wait(0.5)
    splash:runjs("document.getElementsByName('tj_login')[1].click()")
    splash:wait(0.5)
    splash:runjs("document.getElementsByClassName('tang-pass-footerBarULogin')[0].click()")
    return splash:html()
end 
"""


class BaiduLoginSpider(scrapy.Spider):
    name = 'baidu_login'
    allowed_domains = ['www.baidu.com']
    start_urls = 'https://www.baidu.com'

    def parse(self, response):
        pass
#        sel = response.css('div.register_text_tel::text')
#        le = LinkExtractor(attrs='src')
#        src = le.extract_links(response)
#        
#        sel = response.css('div#dialog_tel img')
#        
#        file = open('html.json', 'a')
#        file.write('\n'+str(sel))
#        file.close()
    
    
    # 百度网页的登录页面
    #login_url = 'https://upassport.lianjia.com/dist/js/passport.js'
    user = '18324519124'
    password = 'xiaoXIAO585lj'
        
    def start_requests(self):
        # 首先打开链家首页， 需要渲染 js 页面, 点击 登录
        yield SplashRequest(self.start_urls, endpoint='execute', args={'lua_source':lua_script})
    def login(self, response):
        open_in_browser(response)
        file = open(response.html, 'w')
        file.write(response)
        file.close()
        
        # 下载验证码
        image_urls = 'https://upassport.lianjia.com/freshCaptch'
        yield {'image_urls': [image_urls]}

        formdata = {
            'user': self.user,
            'password' : self.password,
            'code': self.get_captcha_by_OCR(images.path)
        }
        
        yield FormRequest.form_response(login_response, callback=self.parse_login,formdata=formdata, dont_filter=True)
#        login_response = response.meta.get('login_response')
#        
#        if not login_response:
#            # step 1:
#            # 此时 response 为登录页面的响应，从中提取验证码图片的 url 
#            captchaUrl = response.css('label.field.prepend-icon img::attr').extract_first()
#            
#            captchaUrl = response.urljoin(captchaUrl)
#            # 构造 Request 时，将当前 response 保存到 meta 字典中
#            yield Request(captchaUrl, callback=self.login,meta={'login_response':response},dont_filter=True)
#            
#        else:
#            # step 2:
#            # 此时 response 为验证码图片的响应，response.body 是图片的二进制数据
#            formdata = {
#                'email' :self.user,
#                'pass':self.password,
#                # 使用 OCR识别
#                'code':self.get_captcha_by_OCR(response.body),
#            }
#            yield FormRequest.form_response(login_response, callback=self.parse_login,formdata=formdata, dont_filter=True)
#    
        
    def parse_login(self, response):
        pass
#        info = json.loads(response.text)
#        if info['error'] == '0':
#            logger.info('登录成功')
#            return super().start_requests()
#        logger.info('登录失败')
#        return self.start_requests()
    
    def get_captcha_by_OCR(self,data):
        # OCR 识别
        img = Image.open(BytesIO(data))
        img = img.Convert('L')
        captcha = pytesseract.image_to_string(img)
        img.close()
        return captcha