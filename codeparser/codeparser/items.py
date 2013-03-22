from scrapy.item import Item, Field


class ParserItem(Item):
    region_code = Field()
    number_start_range = Field()
    number_end_range = Field()
    name = Field()
    region = Field()
    mobile = Field()
    country = Field()
