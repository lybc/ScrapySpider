# -*- coding: utf-8 -*-
__author__ = 'lybc'

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from xzTieba.items import XztiebaItem

class TiebaSpider(CrawlSpider):
    name = 'tieba'
    start_urls = ['http://tieba.baidu.com/f?kw=%CF%E6%B6%AB%D6%D0%D1%A7&fr=index']
    rules = (
        Rule(LinkExtractor(allow=(r'ie=utf-8\&pn=[^/]+$', )), follow=True),
        Rule(LinkExtractor(allow=('/p/[^/]+$', )), callback='parse_paging')
    )

    def parse_paging(self, response):
        page = response.selector.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[2]/span[2]/text()').extract()
        if page:
            if page[0] > 1:
                for p in range(1, int(page[0])):
                    yield Request(response.url + '?pn=' + str(p), callback=self.parse_item)

    def parse_item(self, response):
        item = XztiebaItem()
        users = response.selector.xpath('//a[@alog-group="p_author"]/text()').extract()
        for user in users:
            # print(str(user.encode('gbk')))
            item['name'] = user
            yield item