# -*- coding: utf-8 -*-
import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from codeparser.items import ParserItem

class KzCodesSpider(BaseSpider):
    name = 'kzcodes'
    start_urls = [u'http://ru.wikipedia.org/wiki/Телефонный_план_нумерации_Казахстана',]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        codes_nodes = hxs.select('//*[@id="mw-content-text"]/ul[32]/li')

        for code_node in codes_nodes:
            item = ParserItem()

            try:
                name = code_node.select('.//a/text()').extract()[0]
            except IndexError:
                name = u'резерв'

            item['region_code'] = code_node.select('.//b/text()').extract()[0]
            item['number_start_range'] = 0
            item['number_end_range'] = 9999999
            item['name'] = name
            item['region'] = u'Казахстан'
            item['country'] = 'KZ'
            item['mobile'] = True

            yield item
