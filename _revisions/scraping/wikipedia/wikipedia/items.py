import scrapy


class WikipediaItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
