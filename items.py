# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PencilnewsItem(scrapy.Item):
    # newsJson = scrapy.Field()
    _id = scrapy.Field()
    newsTitle = scrapy.Field()
    newsContent = scrapy.Field()
    publishDate = scrapy.Field()
    newsSource = scrapy.Field()
    category = scrapy.Field()

    
