#coding=utf-8

from scrapy import Spider
from dotamax.items import DotamaxItem
from scrapy import Request

class DotaTeamSpider(Spider):
    name = 'dotaspider'
    start_urls = [
        'http://dotamax.com/match/tour_famous_team_list/?league_id=&skill=&ladder=&p=1'
    ]

    def parse(self, response):
        namelist = response.xpath('//tr/td[@class="table-title-font"]/text()').extract()
        ranklist = response.xpath('//td[@style="text-align: center;vertical-align: middle;font-weight: 700;color: #fff;"]/text()').extract()
        mmr = response.xpath('//tr//td//div[@style="height: 15px"]/text()').extract()
        k = 0
        for i in range(0, len(namelist)):
            yield DotamaxItem(team_rank=ranklist[i], team_name=namelist[i], team_MMR=mmr[k], team_match=mmr[k+1], rating=mmr[k+2])
            k = k + 3


        for url in range(2, 6):
            tt = "http://dotamax.com/match/tour_famous_team_list/?league_id=&skill=&ladder=&p="+str(url)
            yield Request(tt, callback=self.parse)