# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class NoipSpider(scrapy.Spider):
    name = "noip"
    allowed_domains = ["nbdp.net"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        urls = ['http://lib.nbdp.net/papers.php?p=1',
                'http://lib.nbdp.net/papers.php?p=2',
                'http://lib.nbdp.net/papers.php?p=4',
                'http://lib.nbdp.net/papers.php?p=5'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse2(self, response):
        page = response.url.split("/")[-1]
        filename = 'result/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
#        self.log('Saved file %s' % filename)

    def parse(self, response):
        print('####', response.url)
        next_pages = response.css(
            'div.list-group a::attr(href)').extract()
        for next_page in next_pages:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse2)
