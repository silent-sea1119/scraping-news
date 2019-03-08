# -*- coding: utf-8 -*-
import scrapy
import json
from pencilnews.items import PencilnewsItem
import re

class NewseedSpider(scrapy.Spider):
    name = 'newseed'
    allowed_domains = ['newseed.cn']
    url = "https://news.newseed.cn/p"
    offset = 1
    start_urls = [url + str(offset)]


    def parse(self, response):
        selector = scrapy.Selector(response)
        urls=selector.xpath('//a[@class="title"]/@href').extract()
        for url in urls:
            yield scrapy.Request(url,callback=self.parseDetail)
        self.offset += 1
        if self.offset <= 1:
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parseDetail(self,response):
        selector = scrapy.Selector(response)
        divcontent = selector.xpath('//div[@class="news-content"]')
        body = ""
        for p in divcontent.xpath('.//p/text()'):
            body = body + p.extract()
        if body == "":
            body = divcontent.extract()[0].strip()
            dr = re.compile(r'<[^>]+>',re.S)
            body = dr.sub('',body)
        item = PencilnewsItem()
        item["newsTitle"] = selector.xpath('//h1[@id="title"]/text()').extract()[0]
        item["newsContent"] = body
        item["publishDate"] = selector.xpath('//span[@class="date"]/text()').extract()[0]
        item["newsSource"] = selector.xpath('//span[@class="resfrom"]/text()').extract()[0]
        item["category"] = "none"
        yield item