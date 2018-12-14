# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsSpider(scrapy.Spider):
    name = "shnoip"
    allowed_domains = ["cnblogs.com"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        urls = ['http://shnoip.cnblogs.com/postbody/fulltext.aspx',
                ]
        for url in urls:
            yield scrapy.FormRequest(url=url,
                                     formdata={
                                         'blogapp': 'shnoip',
                                         'postId': '6143587'
                                     },
                                     callback=self.parse)

    def parse(self, response):
        next_pages = response.css(
            'span a::attr(href)').extract()
        for next_page in next_pages:
            if next_page is not None:
                if next_page and next_page.find('html') == -1:
                    print(next_page)
                else:
                    yield response.follow(next_page, callback=self.parse2)

    def parse2(self, response):
        page = response.url.split("/")[-1]
        filename = 'result/shnoip/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
