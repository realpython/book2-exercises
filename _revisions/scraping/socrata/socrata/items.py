import scrapy


class SocrataItem(scrapy.Item):
    text = scrapy.Field()
    url = scrapy.Field()
    views = scrapy.Field()
