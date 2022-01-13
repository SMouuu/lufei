import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ErshouSpider(CrawlSpider):
    name = 'ershou'
    allowed_domains = ['che168.com', 'autohome.com.cn']
    start_urls = ['https://www.che168.com/china/list/#pvareaid=100945']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='viewlist_ul']/li/a"), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//div[@id='listpagination']/a"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
