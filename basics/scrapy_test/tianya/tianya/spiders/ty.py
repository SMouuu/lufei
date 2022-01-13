from sqlite3 import connect
import scrapy
from tianya.items import TianyaItem

class TySpider(scrapy.Spider):
    name = 'ty'
    allowed_domains = ['tianya.cn']
    start_urls = ['http://bbs.tianya.cn/list-worldlook-1.shtml']

    def parse(self, response):
        # print(response.text)
        tbodys = response.xpath(
            "//table[@class='tab-bbs-list tab-bbs-list-2']/tbody")[1:]
        for tbody in tbodys:
            hrefs = tbody.xpath("./tr/td[1]/a/@href").extract()
            for href in hrefs:
                detail_url = response.urljoin(href)
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.detail_parse
                )

        def detail_parse(self,resp):
            t=TianyaItem()
            title=resp.xpath('//*[@id="post_head"]/h1/span[1]/span').extract_first()
            content=resp.xpath('//*[@id="bd"]/div[4]/div[1]/div/div[2]/div[1]/text()').extract_first()
            t['title']=title
            t['content']=content
            yield t
