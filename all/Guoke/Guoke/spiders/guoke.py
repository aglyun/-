# -*- coding: utf-8 -*-

import scrapy
from ..items import GuokeItem
import time


class GuokeSpider(scrapy.Spider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/', ]
    # 控制翻页
    for i in range(100):
        page_url = 'https://www.guokr.com/ask/highlight/?page={}'.format(i+1)
        start_urls.append(page_url)

    def parse(self, response):
        # 这个响应的数据是第一天url的数据
        time.sleep(1)
        r = response.xpath('//div[@class="ask-list-detials"]/h2/a/@href').getall()    # 取出详情页的url
        # 遍历详情页的url
        for url_ in r:
            print(url_)
            # 对每一条详情页的url进行再次请求,callback指向一个回调函数
            yield scrapy.Request(url_, callback=self.parse_url)

    # 回调函数
    def parse_url(self, response):
        """ 这个response里面的数据是详情页的数据"""
        # 从响应中取到标题
        title = response.xpath('//div[@class="post-title"]//h1/text()').get()
        # 从响应中取到一楼的回答
        answer = response.xpath('//div[@class="answer gclear   "][1]/div[@class="answer-r"]/div[@class="answer-txt answerTxt gbbcode-content"]/p/text()').getall()
        # 将列表拼接成字符串
        answer_ = ''.join(answer)
        # 创建管道对象
        item_ = GuokeItem()
        # 保存数据到管道的键值对
        item_['ask_'] = title
        item_['answer_'] = answer_
        # 返回出去，丢给管道那边保存
        yield item_





