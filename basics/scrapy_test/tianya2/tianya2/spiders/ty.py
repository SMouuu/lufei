import scrapy
from scrapy_redis.spiders import RedisSpider
from tianya2.items import Tianya2Item


class TySpider(RedisSpider):
    name = 'ty'
    allowed_domains = ['tianya.cn']
    # start_urls = ['http://tianya.cn/']
    redis_key = "ty_start_url"

    def parse(self, response, **kwargs):
        # print(response.text)
        tbodys = response.xpath(
            "//table[@class='tab-bbs-list tab-bbs-list-2']/tbody")[1:]
        for tbody in tbodys:
            hrefs = tbody.xpath("./tr/td[1]/a/@href").extract()
            for href in hrefs:
                detail_url = response.urljoin(href)
                # 不用判断重复，直接发送，scrapy来判断
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.detail_parse
                )


    def detail_parse(self, resp, **kwargs):
        t = Tianya2Item()
        title = resp.xpath('//*[@id="post_head"]/h1/span[1]/span').extract_first()
        content = resp.xpath('//*[@id="bd"]/div[4]/div[1]/div/div[2]/div[1]/text()').extract_first()
        t['title'] = title.strip()
        t['content'] = content.strip()
        yield t
