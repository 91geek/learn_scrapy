# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from tutorial.items import JaadeeItem


class JaadeeSpider(scrapy.Spider):
    name = "jaadee"
    allowed_domains = ["jaadee.com"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        urls = ['https://www.jaadee.com/xinpin/',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse2(self, response):
        next_pages = response.css('ul.productlistw a::attr(href)').extract()
        yield response.follow(next_pages[0], callback=self.parse3)

    def parse3(self, response):
        print('############', response.url)
        title = response.css('h3.acttitle::text').extract()[0]
        imgs = response.css('ul.actul img::attr(src)').extract()
        market_price = response.css('li.jiag span::text').extract()
        price = response.css('li.huise span::text').extract()
        code = response.css('span.hhao::text').extract()
        remarks = response.css('div.actbbul span::text').extract()
        video = response.css('source::attr(src)').extract()
        item = JaadeeItem(title=title,
                          imgs=imgs,
                          market_price=market_price,
                          price=price,
                          code=code,
                          remarks=remarks,
                          video=video)
        print('###############3', item)
        resutl = {'title': title,
                  'imgs': imgs,
                  'market_price': market_price,
                  'price': price,
                  'code': code,
                  'remarks': remarks,
                  'video': video}
       # print(resutl)
#        next_pages = response.css(
#            'ul.productlistw a::attr(href)').extract()
#        yield response.follow(next_pages[0], callback=self.parse3)
#        self.log('Saved file %s' % filename)

    def parse(self, response):
        next_pages = response.css('div.pmenu_list a::attr(href)').extract()
        yield response.follow(next_pages[0], callback=self.parse2)
 #       print(next_pages)
 #       for next_page in next_pages:
 #           if next_page is not None:
 #               yield response.follow(next_page, callback=self.parse2)
