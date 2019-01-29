# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#声明要爬取的元素，之后再pip与爬虫文件中调用
class FirstpracticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#商品名
    link = scrapy.Field()#链接
    comment= scrapy.Field()#评论
