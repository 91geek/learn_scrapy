# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import json


class NoiNewsSpider(scrapy.Spider):
    name = "noinews"
    allowed_domains = ["noi.cn"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        urls = ['http://www.noi.cn/GetNews.dt?cmd=list&place=%d&psize=10' %
                i for i in range(1, 99)]
        # urls = ['http://www.noi.cn/GetNews.dt?cmd=list&place=2&psize=10']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse2(self, response):
        rs = json.loads(response.text)
        for x in range(0, 10):
            obj = rs.get('%d' % x)
            if obj is not None:
                url = 'http://www.noi.cn/GetNews.dt?cmd=read&newsid=%s&hash=%s' % (obj.get(
                    'id'), obj.get('hash'))
                yield scrapy.Request(url=url, callback=self.parse3)
            else:
                break

    def parse3(self, response):
        rs = json.loads(response.text)
        page = rs.get('id')
        type = rs.get('type')
        title = rs.get('title')
       # print(response.body)
        filename = 'D:\\python_workspace\\learn_scrapy\\tutorial\\result\\noinews\\news_%s_%s_%s.html' % (
            type, page, title)
        with open(filename, 'wb') as f:
            f.write(bytes(rs.get('cont'), 'utf8'))

    def parse(self, response):
        rs = json.loads(response.text)
        next_pages = ['http://www.noi.cn/GetNews.dt?cmd=list&place=1&psize=10&page=%d' %
                      i for i in range(1, int(rs['pagecnt']) + 1)]
        for next_page in next_pages:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse2)
