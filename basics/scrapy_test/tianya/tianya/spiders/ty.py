from sqlite3 import connect
import scrapy
from tianya.items import TianyaItem
from redis import Redis


class TySpider(scrapy.Spider):
    name = 'ty'
    allowed_domains = ['tianya.cn']
    start_urls = ['http://bbs.tianya.cn/list-worldlook-1.shtml']

    def __init__(self, name=None, **kwargs):
        self.red = Redis(host="192.168.75.128", port=6380, db=0, password="123456")
        # 让父类初始化
        super(TySpider, self).__init__(name, **kwargs)

    def parse(self, response, **kwargs):
        # print(response.text)
        tbodys = response.xpath(
            "//table[@class='tab-bbs-list tab-bbs-list-2']/tbody")[1:]
        for tbody in tbodys:
            hrefs = tbody.xpath("./tr/td[1]/a/@href").extract()
            for href in hrefs:
                detail_url = response.urljoin(href)
                # 判断连接是否重复1、直接往redis set里面怼
                # 存在返回1，不存在返回0
                result = self.red.sismember("tianya:ty:detail:url", detail_url)
                if result:
                    print(f"该url已经被抓取过{detail_url}")
                else:
                    yield scrapy.Request(
                        url=detail_url,
                        callback=self.detail_parse
                    )
        page = response.xpath('//div[@class="short-pages-2 clearfix"]/div/a[last()]/@href').extract_first()
        yield scrapy.Request(
            url=response.urljoin(page),
            callback=self.parse
        )

    def detail_parse(self, resp, **kwargs):
        t = TianyaItem()
        title = resp.xpath('//*[@id="post_head"]/h1/span[1]/span').extract_first()
        content = resp.xpath('//*[@id="bd"]/div[4]/div[1]/div/div[2]/div[1]/text()').extract_first()
        t['title'] = title.strip()
        t['content'] = content.strip()
        self.red.sadd("tianya:ty:detail:url", resp.url)
        yield t
