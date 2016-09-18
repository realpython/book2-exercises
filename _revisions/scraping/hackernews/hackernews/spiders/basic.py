from scrapy import Spider
from scrapy.selector import Selector

from hackernews.items import HackernewsItem


class BasicSpider(Spider):
    # name the spider
    name = "basic"

    # allowed domains to scrape
    allowed_domains = ["news.ycombinator.com"]

    # urls the spider begins to crawl from
    start_urls = (
        'https://news.ycombinator.com/',
    )

    # parses and returns the scraped data
    def parse(self, response):
        titles = Selector(response).xpath('//tr[@class="athing"]/td[3]')

        for title in titles:
            item = HackernewsItem()
            item['title'] = title.xpath("a[@href]/text()").extract()
            item['url'] = title.xpath("a/@href").extract()
            yield item
