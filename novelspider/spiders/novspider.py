#-*-coding:utf8-*-
from lxml import etree
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy.http import Request
from novelspider.items import NovelspiderItem
import re

class novSpider(RedisSpider):
    name = "novspider"
    redis_key = 'nvospider:start_urls'
    stockCode = '000555'
    start_urls = ['http://guba.eastmoney.com/list,' + stockCode + ',5_' + str(1) + '.html'
                  ]

    def parse(self,response):
        selector = Selector(response)
        content_field = selector.xpath('//div[@id="articlelistnew"]/div[starts-with(@class,"articleh")]')
        for each in content_field:
            read = each.xpath('span[1]/text()').extract()[0]
            comment = each.xpath('span[2]/text()').extract()[0]
            title = each.xpath('span[3]/a/text()').extract()[0]
            author = each.xpath('span[4]/a/text()').extract()[0]
            date = each.xpath('span[5]/text()').extract()[0]
            last = each.xpath('span[6]/text()').extract()[0]
            address = each.xpath('span[3]/a/@href').extract()[0]
            baseUrl = 'http://guba.eastmoney.com'
            Url = baseUrl+address
            item = NovelspiderItem()
            item['read'] = read
            item['comment'] = comment
            item['title'] = title
            item['author'] = author
            item['date'] = date
            item['last'] = last
            yield Request(Url, callback='parseContent', meta={'item':item})
        info = selector.xpath('//*[@id="articlelistnew"]/div[@class="pager"]/span/@data-pager').extract()[0]
        List = info.split('|')
        # 定义需要抓取多少页
        if int(List[3])<8:
            # 生成页面链接
            nextLink = 'http://guba.eastmoney.com/list,' + '000555' + ',5_' + str(int(List[3])+1) + '.html'
        # 抓取页面并且处理
        yield Request(nextLink,callback=self.parse)

    def parseContent(self, response):
        selector = Selector(response)
        item = response.meta['item']
        data = selector.xpath('//div[@class="stockcodec"]')
        info = data.xpath('string(.)').extract()[0]
        item['text'] = info
        yield item