import scrapy


class ShuangseqiuSpider(scrapy.Spider):
    name = 'shuangseqiu'
    allowed_domains = ['500.com']
    start_urls = ['http://500.com/']

    def parse(self, response):
        pass
