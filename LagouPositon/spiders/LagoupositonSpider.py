# -*- coding: utf-8 -*-
import scrapy
import json
from LagouPositon.items import LagoupositonItem

class LagoupositonSpider(scrapy.Spider):
    name = "Lagoupositon"
    curpage = 1
    #allowed_domains = ["http://www.lagou.com/zhaopin/"]
    start_urls = (
        'http://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false',
    )

    def parse(self, response):
       #fp = open('lagou.html','w')
       #fp.write(response.body)
       #fp.close()
       #print response.body
        item = LagoupositonItem()
        jdict = json.loads(response.body)
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        jresult = jposresult["result"]
        for each in jresult:
            item['city'] =  each['city']
            item['leaderName'] = each['leaderName']
            item['positionFirstType'] = each['positionFirstType']
            item['positionAdvantage'] = each['positionAdvantage']
            item['companyShortName'] = each['companyShortName']
            item['companySize'] = each['companySize']
            item['positionName'] = each['positionName']
            item['positionType'] = each['positionType']
            item['salary'] = each['salary']
            item['createTime'] = each['createTime']
            yield item

            self.totalPageCount = jposresult['totalCount'] / 15
            if self.totalPageCount > 30:
                self.totalPageCount = 30

            if self.curpage <= self.totalPageCount:
                self.curpage += 1
            yield scrapy.http.FormRequest('http://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false',
                                          formdata={'pn': str(self.curpage)}, callback=self.parse)
