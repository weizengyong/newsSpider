# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import datetime
import os
def  CreateDateFolder():
	now=datetime.datetime.now()
	strTime=now.strftime("%Y-%m-%d")
	strPath="./downloadfile/%s"%strTime
	if  not os.path.exists(strPath):
		os.mkdir(strPath)
	return strPath
class NewsspiderPipeline(object):
 	def process_item(self, item, spider):
 		strPath=CreateDateFolder()
 		if item['title']:
 			fileName=''.join(item['title'])
 			file=codecs.open('%s/%s'%(strPath,fileName),'w',encoding='utf-8')
 			#file.write(item['url'])
 			file.write(item['content'])
 			file.close()
        		return item
        	else:
        		raise DropItem("empty" )

