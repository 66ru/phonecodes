import re
from scrapy.spider import BaseSpider
from codeparser.items import ParserItem


class CodesSpider(BaseSpider):
    name = 'codes'

    start_urls = [
        'http://www.rossvyaz.ru/docs/articles/ABC-3x.html',
        'http://www.rossvyaz.ru/docs/articles/ABC-4x.html',
        'http://www.rossvyaz.ru/docs/articles/ABC-8x.html',
        'http://www.rossvyaz.ru/docs/articles/DEF-9x.html',
    ]

    def parse(self, response):
        t_rows = re.findall(r'<tr>(.*?)</tr>', response.body.decode('cp1251'))
        for t_row in t_rows:
            item = ParserItem()
            item_list = re.findall(r'<td>(.*?)</td>', t_row)
            if item_list:
                item_list = [i.replace('\t', '') for i in item_list]
                item['region_code'] = item_list[0]
                item['number_start_range'] = item_list[1]
                item['number_end_range'] = item_list[2]
                item['name'] = item_list[4]
                item['region'] = item_list[5]
                item['country'] = 'RU'

                if response.url == 'http://www.rossvyaz.ru/docs/articles/DEF-9x.html':
                    item['mobile'] = True
                else:
                    item['mobile'] = False

                yield item
