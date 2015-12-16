from scrapy import Spider
from scrapy.selector import Selector
from urlparse import urljoin

from wikipedia.items import WikipediaItem


class BasicSpider(Spider):
    # name the spider
    name = "wiki"

    # allowed domains to scrape
    allowed_domains = ["en.wikipedia.org"]

    # urls the spider begins to crawl from
    start_urls = (
        "http://en.wikipedia.org/wiki/Category:2014_films",
    )

    # parses and returns the scraped data
    def parse(self, response):

        titles = Selector(response).xpath('//div[@id="mw-pages"]//li')

        for title in titles:
            item = WikipediaItem()
            url = title.select("a/@href").extract()
            if url:
                item["title"] = title.select("a/text()").extract()
                item["url"] = urljoin("http://en.wikipedia.org", url[0])
                yield item