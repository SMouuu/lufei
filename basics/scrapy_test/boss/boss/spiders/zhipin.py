import scrapy
from boss.request import SeleniumRequest

class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101020100&industry=&position=']

    def start_requests(self):
        yield SeleniumRequest(
            url=self.start_urls[0],
            callback=self.parse
        )
        pass


    def parse(self, response):
        pass
