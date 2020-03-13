# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import json
import math

#云南省公共资源交易中心
class DHSpider(scrapy.Spider):
    name = "ynggzy"
    allowed_domains = ["ynggzy.com"]

    def start_requests(self):
        url = 'https://www.ynggzy.com/jyxx/jsgcZbgg'
        formdata = {
               
                    }
        yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse)
    def parse(self, response):
        totlePageCount = response.xpath('//div[@class= "mmggxlh"]/a/text()').extract()[-2]
        totlePageCount = 2
        url = 'https://www.ynggzy.com/jyxx/jsgcZbgg'
        for i in range(1,totlePageCount):
            formdata = {
                          'currentPage':str(i),
                          'area':'0',
                          'industriesTypeCode':'0',
                          'scrollValue':'700'
            }
            yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse2)
    def parse(self, response):
        next_pages=  response.xpath('//tbody/tr/td/a/attribute::href').extract()
        for next_page in next_pages:
            yield response.follow(next_page, callback=self.parse2)
    def parse2(self, response):
       # print(response.url)
        title = response.xpath('//h3[@class="detail_t"]/text()').extract()[0]
        detail = response.xpath('//table/tr/td[text()="本次招标内容："]/following-sibling::*/span/text()').extract()[0]
        print("########",detail)
       
        





    
