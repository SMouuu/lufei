import scrapy


class TySpider(scrapy.Spider):
    name = 'ty'
    allowed_domains = ['tianya.cn']
    start_urls = ['http://tianya.cn/']

    def parse(self, response):
        pass
