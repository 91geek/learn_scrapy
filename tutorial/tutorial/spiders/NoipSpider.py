# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NoipSpider(scrapy.Spider):
    name = "noip"
    #allowed_domains = ["nbdp.net"]
    #start_urls = ["http://lib.nbdp.net/"]
        def start_requests(self):
            urls = ["http://lib.nbdp.net/"]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
