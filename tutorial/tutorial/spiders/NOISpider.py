# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NoiSpider(scrapy.Spider):
    name = "noi"
    allowed_domains = ["noi.cn"]
    # start_urls = ["http://lib.nbdp.net/"]

    def start_requests(self):
        urls = ['http://oj.noi.cn/oj/index.php/main/problemset/%d?seed=0.4680022332267537' %
                i for i in range(1, 26)]
        cookies = {'priviledge': 'user'}
        cookies = {'foj_ci_session': '7ad1c958239610d57bd7c4f97e966f0e4a79e313'}
     #   urls = [
     #       'http://oj.noi.cn/oj/index.php/main/problemset/3?seed=0.4680022332267537']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)

    def parse2(self, response):
      #  print('###########', response.url)
        page = response.url.split("/")[-1].split('?')[0]
       # print(page)
        filename = 'result/oj.noi.cn/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

    def parse(self, response):
        next_pages = response.css('tr td.title a::attr(href)').extract()
      #  print(next_pages)
        for next_page in next_pages:
            if next_page is not None:
                next_page = 'http://oj.noi.cn/oj/index.php/%s?&?seed=0.4680022332267537' % next_page[1:]
                yield response.follow(next_page, callback=self.parse2)
