from scrapy import Spider
from scrapy.selector import Selector

from socrata.items import SocrataItem


class OpendataSpider(Spider):
    name = "opendata"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = (
        'https://opendata.socrata.com/',
    )

    def parse(self, response):
        titles = Selector(response).xpath('//tr[@itemscope="itemscope"]')
        for title in titles:
            item = SocrataItem()
            item["text"] = title.select("td[2]/div/span/text()").extract()
            item["url"] = title.select("td[2]/div/a/@href").extract()
            item["views"] = title.select("td[3]/span/text()").extract()
            yield item
