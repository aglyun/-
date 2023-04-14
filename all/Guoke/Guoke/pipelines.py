# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json 

class GuokePipeline:
    def __init__(self):
        print('文件打开啦')
        self.file = open('问答_2.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print('文件开始保存数据啦...')
        item_ = dict(item)
        item_json = json.dumps(item_, ensure_ascii=False)+',\n'

        self.file.write(item_json)
        return item

    def __del__(self):
        print('文件关闭啦')
        self.file.close()
