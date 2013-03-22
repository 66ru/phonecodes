# -*- coding: utf-8 -*-
from urlparse import urlparse
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from codeparser.items import ParserItem


class KzCodesSpider(BaseSpider):
    name = 'kzcodes'
    start_urls = [u'http://ru.wikipedia.org/wiki/Телефонный_план_нумерации_Казахстана',
                  u'http://spravkaru.net/kazahstan/codes/']

    def parse(self, response):
        domain = response.url.replace(urlparse(response.url).path, '')
        hxs = HtmlXPathSelector(response)

        codes_nodes = hxs.select('//*[@id="mw-content-text"]/ul[32]/li')
        city_codes_links = hxs.select('//div[@id="data"]/p[2]/a[@class="decor_link"]/@href')

        if codes_nodes:
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

        if city_codes_links:
            for link in city_codes_links:
                yield Request(domain + link.extract(), self.parse_citycodes)

    def parse_citycodes(self, response):
        hxs = HtmlXPathSelector(response)
        codes_nodes = hxs.select('//*[@id="data"]/table/tr')

        for code_node in codes_nodes[1:]:
            item = ParserItem()

            name = code_node.select('.//td[1]/text()').extract()[0]
            code = int(code_node.select('.//td[2]/text()').extract()[0])
            number = code_node.select('.//td[4]/text()').extract()[0][1:]
            number = number.replace(' ', '')
            number = number.replace('(', '')
            number = number.replace(')', '')
            number = number.replace('-', '')

            item['region_code'] = int(code)
            item['number_start_range'] = int(number.replace('X', '0'))
            item['number_end_range'] = int(number.replace('X', '9'))
            item['name'] = name
            item['region'] = u'Казахстан'
            item['country'] = 'KZ'
            item['mobile'] = False

            yield item
