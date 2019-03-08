import json
import pymongo
from scrapy.conf import settings

class PencilnewsPipeline(object):
    def __init__(self):
        # self.filename = open("pencilnews.json", "w")
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]
    def process_item(self, item, spider):
        self.post.insert_one(item)
        return item

    # def close_spider(self, spider):
    #     self.filename.close()


class xfzPipeline(object):
    def __init__(self):
        # self.filename = open("pencilnews.json", "w")
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME_XFZ"]
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]
    def process_item(self, item, spider):
        self.post.insert_one(item)
        return item

class newseedPipeline(object):
    def __init__(self):
        # self.filename = open("pencilnews.json", "w")
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME_NEWSEED"]
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]
    def process_item(self, item, spider):
        self.post.insert_one(item)
        return item