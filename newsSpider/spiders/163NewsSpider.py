# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from newsSpider.items import NewsspiderItem
class newsSpider(CrawlSpider):
	name="163NewsSpider"
	allowed_domains=["163.com"]
	start_urls=["http://news.163.com/domestic/",
	"http://news.163.com/shehui/"]
	rules=[
	Rule(sle(allow=("http://news.163.com/special/0001124J/[^/]+headList$"))),
	Rule(sle(allow=("http://news.163.com/15/\d{4}/\d{2}/[^/]+")),callback='parse_news'),
	]
	def parse_news(self,response):
		item=NewsspiderItem()
		item['url']=response.url
		sel=Selector(response)
		item['title']=sel.xpath("//h1[@id='h1title']/text() ").extract()
		pags=sel.xpath("//div[@id='endText']/p")
		strContent=u''
		for p in pags:
			strContent+=u''.join(p.xpath("text()").extract())+u"\n"
		item['content']=strContent
		return item


