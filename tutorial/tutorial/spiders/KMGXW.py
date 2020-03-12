# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 昆明工信局信息爬取
import scrapy
from tutorial.items import NewsItem

class KMGXJSpider(scrapy.Spider):
    name = "km_gxj"  #昆明工信委
    allowed_domains = ["gxj.km.gov.cn"]
    all_title = []
    sum = 0
    def start_requests(self):
        urls = ['http://gxj.km.gov.cn/zcms/catalog/15575/pc/index_%d.shtml' % i for i in range(1, 85)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        next_pages = response.css('div.list_txtsbg a::attr(href)').extract()
        if next_pages is not None and len(next_pages) > 0 :
            for next_page in next_pages:
                yield response.follow(next_page, callback=self.parse2,dont_filter=True)
        else:
            self.sum = self.sum + 1
            print(self.sum,"####",response.url)
        
       # for next_page in next_pages:
       #     yield response.follow(next_page, callback=self.parse2)
       # yield response.follow(next_pages[0], callback=self.parse2,dont_filter=True)
    def parse2(self, response):
        if response is not None:
            url = response.url;
            title = response.xpath('//div[@class= "timu"]/text()').extract()[0]
            date = response.xpath('//div[@class= "time"]/span/text()').extract()[0]
            tt = response.xpath('//div[@class= "txtcen"]')
            detail = tt.xpath("string(.)").extract()[0]
            detail = detail.replace(' ','')
            detail = detail.replace('\xa0\r\n','')
            item = NewsItem(title=title,
                          url=url,
                          date=date,
                          detail=detail)
            yield item
