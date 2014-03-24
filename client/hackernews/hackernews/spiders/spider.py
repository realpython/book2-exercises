# spider.py


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hackernews.items import HackernewsItem

class MySpider(BaseSpider):

    # name the spider
    name = "hackernews"

    # allowed domains to scrape
    allowed_domains = ["news.ycombinator.com/"]

    # urls the spider begins to crawl from
    start_urls = ["https://news.ycombinator.com/"]

    # parses and returns the scraped data
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//td[@class="title"]')
        items = []
        for title in titles:
            item = HackernewsItem()
            item["title"] = title.select("a/text()").extract()
            item["url"] = title.select("a/@href").extract()
            items.append(item)
        return items
