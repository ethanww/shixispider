# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 文章名
    time = scrapy.Field()  # 发帖时间
    author = scrapy.Field()  # 发帖人
    description= scrapy.Field()  # 内容描述
