# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JaadeeItem(scrapy.Item):
    url = scrapy.Field()
    html = scrapy.Field()
    title = scrapy.Field()
    remarks = scrapy.Field()
    imgs = scrapy.Field()
    code = scrapy.Field()
    price = scrapy.Field()
    market_price = scrapy.Field()
    video = scrapy.Field()
