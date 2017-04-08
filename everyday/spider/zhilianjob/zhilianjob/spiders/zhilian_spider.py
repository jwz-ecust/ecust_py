# -*- coding: utf-8 -*-

import scrapy
from zhilianjob.items import ZhilianjobItem


class ZhilianSpider(scrapy.Spider):
    name = "zhilian"
    s = 0

    start_urls = [
        "http://www.zhaopin.com/citymap.html"
    ]

    def parse(self, response):
        for cities in response.xpath("//*[@id='letter_choose']/dl/dd"):
            for city in cities.xpath(".//a"):
                if city.xpath('.//strong').extract_first() is not None:
                    city = city.xpath(".//strong")
                ct = city.xpath(".//text()").extract_first()
                url_python = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&sm=0&p=1' % (ct, u"化学")
                yield scrapy.Request(url=url_python, callback=self.parse_python)

    def parse_python(self, response):
        job_position = response.xpath('//*[@id="JobLocation"]/@value').extract_first()
        # print job_position
        # 公司名称， 地点， 公司性质， 学历， 月薪， 工作内容
        for job in response.xpath('//table[@class="newlist"]/tr'):
            kword = job.xpath('.//td[@class="zwmc"]/div/a/b/text()').extract_first()
            if kword is not None:
                item = ZhilianjobItem()
                item['job_company'] = job.xpath('.//td[@class="gsmc"]/a/text()').extract_first()
                item['job_price'] = job.xpath('.//td[@class="zwyx"]/text()').extract_first()
                item['job_date'] = job.xpath('.//td[@class="gxsj"]/span/text()').extract_first()
                item['job_position'] = job_position
                item['job_name'] = job.xpath('.//td[@class="zwmc"]/div/a/text()').extract_first()
                item['job_is'] = 1
                yield item
            python_next = response.xpath("//div[@class='pagesDown']/ul/li[3]/a").extract_first()
            if python_next is not None:
                yield scrapy.Request(url=python_next, callback=self.parse_python)
