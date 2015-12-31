# -*- coding: utf-8 -*-
__author__ = 'lybc'

from scrapy.spiders import Spider
from scrapy.http import Request
from xzTieba.items import XztiebaItem

class user_spider(Spider):
    name = 'userSpider'
    start_urls = ['http://tieba.baidu.com/f/like/furank?kw=%E6%B9%98%E4%B8%9C%E4%B8%AD%E5%AD%A6&ie=utf-8#p']

    def parse(self, response):
        base_url = 'http://tieba.baidu.com/f/like/furank?kw=%CF%E6%B6%AB%D6%D0%D1%A7&pn='
        for page in range(1, 363):
            url = base_url + str(page)
            yield Request(url, callback=self.parse_user)

    def parse_user(self, response):
        base_url = 'http://tieba.baidu.com'
        top = response.selector.xpath("//a[@class='drl_item_name_top']/@href").extract()
        if top:
            for t in top:
                yield Request(url=base_url+t, callback=self.parse_items)
        normal = response.selector.xpath("//a[@class='drl_item_name_nor']/@href").extract()
        for n in normal:
            yield Request(url=base_url+n, callback=self.parse_items)

    def parse_items(self, response):
        items = XztiebaItem()
        name = response.selector.xpath('//*[@id="userinfo_wrap"]/div[2]/div[2]/span/text()').extract()[0]
        age = response.selector.xpath('//*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[2]/text()').extract()[0]
        count = response.selector.xpath('//*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[4]/text()').extract()[0]
        items['name'] = name
        age = age.split(':')[1]
        if u"年" in age:
            age = float(age[:-1]) * 365
        items['age_day'] = age
        count = count.split(':')[1]
        if u"万" in count:
            count = float(count[:-1]) * 10000
        else:
            count = float(count)
        items['count'] = count
        items['avg'] = count / age
        return items


