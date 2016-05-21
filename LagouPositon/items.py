# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagoupositonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    leaderName = scrapy.Field()
    positionFirstType = scrapy.Field()
    positionAdvantage = scrapy.Field()
    companyShortName = scrapy.Field()
    companySize = scrapy.Field()
    positionName = scrapy.Field()
    positionType = scrapy.Field()
    salary = scrapy.Field()
    createTime = scrapy.Field()

