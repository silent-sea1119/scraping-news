# -*- coding: utf-8 -*-
import scrapy
from pencilnews.items import PencilnewsItem
import json
import re


class XfznewsSpider(scrapy.Spider):
    name = 'xfznews'
    allowed_domains = ['xfz.cn']
    url = "https://www.xfz.cn/api/website/articles/?n=20&type=&p="
    offset = 1
    start_urls = [url + str(offset)]
    def parse(self, response):
        result = json.loads(response.body.decode().strip())
        if(result["code"]== 200):
            index = 0
            items = result["data"]
            while index < 20:
                uid = items[index]["uid"]
                detialurl = "https://www.xfz.cn/post/" + str(uid) + ".html"
                yield scrapy.Request(detialurl, callback=self.parseDetail)
                index += 1
                # yield item
        self.offset += 1
        if self.offset <= 100:
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


    def parseDetail(self, response):
        selector = scrapy.Selector(response)

        divcontent = selector.xpath('//div[@class="content-detail"]')
        body = ""
        for p in divcontent.xpath('.//p/text()'):
            body = body + p.extract()
        if body == "":
            body = divcontent.extract()[0].strip()
            dr = re.compile(r'<[^>]+>',re.S)
            body = dr.sub('',body)
        item = PencilnewsItem()
        item["newsTitle"] = selector.xpath('//h1[@class="title"]/text()').extract()[0]
        item["newsContent"] = body
        item["publishDate"] = selector.xpath('//span[@class="time"]/text()').extract()[0]
        item["newsSource"] = selector.xpath('//span[@class="author-name"]/text()').extract()[0]
        item["category"] = "none"
        yield item