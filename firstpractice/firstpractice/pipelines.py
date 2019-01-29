# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

    #1、先在settings中开启此类
    #2、传至数据库
class FirstpracticePipeline(object):
    def process_item(self, item, spider):
        #这里可以连接数据库
        #connect = pymysql.connect()
        for i in range(0,len(item["title"]),1):#将爬取的对应位置不同特征进行合并
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            print(title,"+",link,"+",comment)
            #sql = "insert into hello(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            #connect.query(sql)
        #connect.close()
        return item
