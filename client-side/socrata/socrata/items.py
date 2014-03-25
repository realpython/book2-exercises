from scrapy.item import Item, Field

class SocrataItem(Item):
    text = Field()
    url = Field()
    views = Field()
