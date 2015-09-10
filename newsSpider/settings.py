# -*- coding: utf-8 -*-

# Scrapy settings for newsSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newsSpider'

SPIDER_MODULES = ['newsSpider.spiders']
NEWSPIDER_MODULE = 'newsSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsSpider (+http://www.yourdomain.com)'
DOWNLOAD_DELAY=2.0
#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'newsSpider.rotate_useragent.RotateUserAgentMiddleware' :400,
 }
ITEM_PIPELINES={'newsSpider.pipelines.NewsspiderPipeline':300,}