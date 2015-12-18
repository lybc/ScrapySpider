import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import time
from vcsoGrid.items import VcsogridItem

class ImageSpider(scrapy.spiders.Spider):
	name = 'vsco'

	def __init__(self):
		self.browser = webdriver.Chrome()


	def start_requests(self):
		base_url = 'http://grid.vsco.co/grid/'
		for i in range(1, 4081):
			url = base_url + str(i)
			yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
		self.browser.get(response.url)
		time.sleep(3)
		page = self.browser.page_source
		imgs = Selector(text=page).select('//img/@src').extract()
		item = VcsogridItem()

		for img in imgs:
			if '.jpg?' in img:
				src = img.split("?")
				item['image_urls'] = ['http:' + str(src[0])]
				yield item

	def __del__(self):
		self.browser.close()
