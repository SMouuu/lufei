import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ErshouSpider(CrawlSpider):
    name = 'ershou'
    allowed_domains = ['che168.com', 'autohome.com.cn']
    start_urls = ['https://www.che168.com/china/list/#pvareaid=100945']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='viewlist_ul']/li/a"), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//div[@id='listpagination']/a"), follow=True)
    )

    def parse_item(self, resp):
        # 处理详情页
        title = resp.xpath("//div[@class='car-box']/h3/text()").extract_first()
        price = resp.xpath("//span[@id='overlayPrice']/text()").extract_first()
        print(title, price)
