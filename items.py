# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticeItem(scrapy.Item):
    #存储图片名字
    name = scrapy.Field()
    #存储图片的链接
    ImgUrl = scrapy.Field()
    pass
