import scrapy


class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    def parse(self, response):
        pass
