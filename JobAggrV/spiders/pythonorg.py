import scrapy


class PythonorgSpider(scrapy.Spider):
    name = 'pythonorg'
    allowed_domains = ['www.python.org']
    start_urls = ['http://www.python.org/']

    def parse(self, response):
        pass
