# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import json
import math

#东方航空爬虫
class DHSpider(scrapy.Spider):
    name = "YNBid"
    allowed_domains = ["yngp.com"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        url = 'http://www.yngp.com/bulletin.do?method=moreListQuery'
        formdata = {
                     'current':'1',
                     'rowCount':'2',
                     'query_sign':'1'
                    }
        yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse)
    def parse(self, response):
        rs = json.loads(response.text)
        url = 'http://www.yngp.com/bulletin.do?method=moreListQuery'
        totlePageCount = math.ceil(rs["total"] / 200.0)
        for i in range(1,m):
            formdata = {
                     'current': str(i,totlePageCount),
                     'rowCount':'200',
                     'query_sign':'1'
                    }
            yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse2)
    
    def parse2(self, response):
         rs = json.loads(response.text)
         rows = rs['rows']
         for row in rows:
             next_page ='http://www.yngp.com/newbulletin_zz.do?method=preinsertgomodify&operator_state=1&flag=view&bulletin_id='+row
             yield response.follow(next_page, callback=self.parse3,dont_filter=True)
             print(row['bulletin_id'])




    
