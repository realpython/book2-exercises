from scrapy.item import Item, Field

class WikipediaItem(Item):
    title = Field()
    url = Field()
