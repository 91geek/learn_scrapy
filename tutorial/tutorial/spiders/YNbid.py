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
        totlePageCount = 2
        for i in range(1,totlePageCount):
            formdata = {
                     'current': str(i),
                     'rowCount':'200',
                     'query_sign':'1'
                    }
            yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse2)
    
    def parse2(self, response):
         rs = json.loads(response.text)
         rows = rs['rows']
         for row in rows:
             next_page ='http://www.yngp.com/newbulletin_zz.do?method=preinsertgomodify&operator_state=1&flag=view&bulletin_id='+row['bulletin_id']
             yield response.follow(next_page, callback=self.parse3,dont_filter=True)
    def parse3(self, response):
        title = response.xpath('//div[@class= "col-xs-8 control-label-text"]/text()').extract()[0].strip()
      #  filename = '/Users/wanglei/Documents/python/learn_scrapy/doc/%s.html' % (title)
      #  with open(filename, 'wb') as f:
      #      f.write(bytes(response.text, 'utf8'))
        selected = response.xpath('//div[@id="gglx_div"]/div/select/option[@selected]')
        typeName = selected.xpath('text()').extract()[0].strip()
        type = selected.xpath('attribute::value').extract()[0]
        
       # print(tt)
       # type = tt.xpath("string(.)")
        print(title,typeName)




    
