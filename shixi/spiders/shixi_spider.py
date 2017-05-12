#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy import Request,FormRequest
from shixi.items import ShixiItem
from shixi.transTime import trans_time

class ShixiSpider(Spider):
    name = 'shixi'
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    allowed_domains = ["newsmth.net"]  # 水木清华
    base_url = 'http://www.newsmth.net'  # 水木清华的基本URL，用于后面的组装
    urls_list = []  # 将所有子文章放置在该list里面
    inter_num = 10  # 选取10页文章内容
    inter_now = 1  # 当前爬取的页数

    cookie = {'main[UTMPKEY]': '60686729',
              'main[PASSWORD]': 'TsrjVL%2506O%25044r%2522%2505f%255C%25193%2503%2502V%2525p%250D%255E',
              'Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567': '1494552866',
              'Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567': '1493100709,1493624270,1494404344',
              'main[XWJOKE]': 'hoho',
              'left-index': '00000100000',
              'main[UTMPNUM]': '13826',
              'NFORUM': 'ak4njd9s73hkqd487brrkfd8u6',
              'main[UTMPUSERID]': 'ethanww',
              'left-show': '0'}


    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    # 爬虫的起点
    def start_requests(self):
        url = 'http://www.newsmth.net/nForum/board/Intern'  # 水木清华实习信息页面
        yield Request(url=url,headers=self.headers,cookies=self.cookie,meta=self.meta,callback=self.parse_urls)


    def parse_urls(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        urls = response.xpath('//table/tbody/tr/td[2]/a/@href').extract()  # 找到当前页面上帖子的url
        self.urls_list.extend(urls)  # 将找到的url都放置到list中去
        if self.inter_now < self.inter_num:
            self.inter_now += 1
            next_url = '/nForum/board/Intern?p=%d' % self.inter_now
            next_abs_url = self.base_url + next_url
            yield Request(url=next_abs_url,headers=self.headers,cookies=self.cookie,meta=self.meta,callback=self.parse_urls)
        while len(self.urls_list) > 0:
            post_next_url = self.urls_list.pop()
            post_abs_url = self.base_url + post_next_url
            yield Request(url=post_abs_url,headers=self.headers,cookies=self.cookie,meta=self.meta,callback=self.post_item)

    #
    # def post_urls(self,response):
    #     while len(self.urls_list) > 0:
    #         post_next_url = self.urls_list.pop()
    #         post_abs_url = self.base_url + post_next_url
    #         yield Request(url=post_abs_url,headers=self.headers,cookies=self.cookie,meta=self.meta,callback=self.post_item)

    def post_item(self,response):
        item=ShixiItem()
        item['title'] = response.xpath('//div[1]//p/text()[2]').extract()
        item['time'] = trans_time(str(response.xpath('//div[1]//p/text()[3]').extract()))
        item['author'] = response.xpath('//div[1]//p/text()[1]').extract()
        item['description'] = response.xpath('//div[1]//p/text()').extract()
        yield item

    # def parse(self, response):
    #     item = ShixiItem()











