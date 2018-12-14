# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpenJudgeSpider(scrapy.Spider):
    name = "openjudge"
    allowed_domains = ["openjudge.cn"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        urls = ['http://openjudge.cn/groups',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse2(self, response):
        next_pages = response.css('div.main-content  a::attr(href)').extract()
        for next_page in next_pages:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse3)

    def parse3(self, response):
        next_pages = response.css('tbody tr td  a::attr(href)').extract()
        for next_page in next_pages:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse4)

    def parse4(self, response):
        page = response.xpath('//h2/text()').extract()
        print(response.url, '###################', page[1])
        if page is not None:
            filename = 'result/openjudge/%s.html' % page[1].replace(':', '_')
            with open(filename, 'wb') as f:
                f.write(response.body)

    def parse(self, response):
        next_pages = response.css(
            'div#main li a::attr(href)').extract()
#        print(next_pages)
#        yield response.follow(next_pages[1], callback=self.parse2)
        for next_page in next_pages:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse2)
