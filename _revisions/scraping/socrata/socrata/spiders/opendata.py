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
        titles = Selector(response).xpath('//div[@itemscope="itemscope"]')
        for title in titles:
            item = SocrataItem()
            item["text"] = title.xpath('.//div[@class="browse2-result-title"]/h2/a/text()').extract()[0]
            item["url"] = title.xpath('.//div[@class="browse2-result-title"]/h2/a/@href').extract()[0]
            item["views"] = title.xpath('.//div[@class="browse2-result-view-count-value"]/text()').extract()[0].strip()
            yield item
