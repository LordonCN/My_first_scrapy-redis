# -*- coding: utf-8 -*-
import scrapy
from firstpractice.items import FirstpracticeItem #注意地址这么写，爆红没关系
from scrapy.http import Request#注意   与平时的不同
class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    #找到页数的规律进行多页爬取
    start_urls = ['http://category.dangdang.com/pg1-cid10009438.html']#开始的第一页

    def parse(self, response):#相当于自动request，返回的值为response
        #此处 实例化类，创建容器 将字段导入
        item = FirstpracticeItem()
        item["title"] = response.xpath('//div[@id="search_nature_rg"]/ul/li/a/@title').extract() #使用xpath并解压
        item["link"] = response.xpath('//div[@id="search_nature_rg"]/ul/li/a/@href').extract()
        item["comment"] = response.xpath('//div[@id="search_nature_rg"]/ul/li/p[last()-1]/a/text()').extract()
        #写入数据库中，交给pipelines处理
        yield item
        #循环多页爬取
        for i in range(2,81):#目标爬取页数
            try:#异常处理
                url = 'http://category.dangdang.com/pg'+str(i)+'-cid10009438.html'#构造
            except Exception as err:
                print(err)
            yield Request(url,callback = self.parse)#爬取网址+回调函数传至pip 注意