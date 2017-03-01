# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DotamaxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    team_rank = scrapy.Field()
    team_name = scrapy.Field()
    team_MMR = scrapy.Field()
    team_match = scrapy.Field()
    rating = scrapy.Field()
    team_member = scrapy.Field()
