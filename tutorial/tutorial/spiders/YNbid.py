# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import json
import math

#云南省政府采购网
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
                     'rowCount':'4',
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
        bt_be_2 = response.xpath('//div[@id="bt_be_2"]/div/div/text()').extract()[0].strip()
        start_date = bt_be_2.split('至')[0]
        end_date = bt_be_2.split('至')[1]
        org = response.xpath('//div[@id="pn_pn"]/div/text()').extract()[0].strip()
        contact = response.xpath('//div[@id="pcn_pcp"]/div/text()').extract()[0].strip()
        contect_num = response.xpath('//div[@id="pcn_pcp_2"]/div/text()').extract()[0].strip()
        unit = response.xpath('//div[@id="hiddenCgr"]/div/text()').extract()[0].strip()
        address = response.xpath('//div[@id="hiddenCgr_2"]/div/text()').extract()[0].strip()
        bcsq=response.xpath('//div[@id="bcsq"]/div/text()').extract()[0].strip() #资格要求
        e=response.xpath('//div[@id="e"]/div/text()').extract()[0].strip() #采购需求、数量、简要技术要求
        money=response.xpath('//div[@id="bcb"]/div/text()').extract()[0].strip() #预算金额
        closing_time=response.xpath('//div[@id="bcct"]/div/text()').extract()[0].strip() #投标截止时间/谈判响应文件递交截止时间/询价公告审查资质的时间
        opening_time =response.xpath('//div[@id="bcot"]/div/text()').extract()[0].strip() #预算金额
        detail =response.xpath('//div[@id="UserDetails"]/div/p')#详情
        detail =''.join(detail.xpath('string(.)').extract())






    
