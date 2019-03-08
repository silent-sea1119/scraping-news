# -*- coding: utf-8 -*-
import scrapy
import json
from pencilnews.items import PencilnewsItem
import chardet



class PencilnewsSpider(scrapy.Spider):
    name = 'pencilNews'
    allowed_domains = ['pencilnews.cn']
    # start_urls = ['http://pencilnews.cn/']
    url = "https://api.pencilnews.cn/news?page="
    offset = 1
    start_urls = [url + str(offset)]
    pages = 10
    page_size = 10
    def parse(self, response):
        result = json.loads(response.body.decode().strip())
        if(result["code"] == 1000):
            pages = result["data"]["page_info"]["pages"]
            page_size = result["data"]["page_info"]["page_size"]
            index = 0
            items = result["data"]["lists"]
            while index < page_size:
                item = PencilnewsItem()
                # item["newsJson"] = items[index]
                item["newsTitle"] = items[index]["title"]
                item["newsContent"] = items[index]["digest"]
                item["publishDate"] = items[index]["created_at"]
                item["newsSource"] = items[index]["channel"]
                item["category"] = "none"
                index += 1
                yield item
        self.offset += 1 
        if self.offset <= pages:
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    