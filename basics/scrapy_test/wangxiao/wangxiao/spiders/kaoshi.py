import scrapy
from scrapy.linkextractors import LinkExtractor


class KaoshiSpider(scrapy.Spider):
    name = 'kaoshi'
    allowed_domains = ['wangxiao.cn']
    start_urls = ['https://ks.wangxiao.cn/']

    def parse(self, response, **kwargs):
        le = LinkExtractor(restrict_xpaths="//ul[@class='first-title']/li/div/a")
        a_list = le.extract_links(response)
        for a in a_list:
            fist_title = a.text
            exampoint_url = a.url.replace("TestPaper", "exampoint")

            yield scrapy.Request(
                url=exampoint_url,
                callback=self.parse_sencod_level,
            )

    def parse_sencod_level(self, resp):
        le = LinkExtractor(restrict_xpaths="//div[@class='filter-content']/div[2]/a")
        a_list = le.extract_links(resp)
        for a in a_list:
            #进入第三层
            yield scrapy.Request(
                url=a.url,
                callback=self.parse_third_level,
            )


    def parse_third_level(self,resp):
        points=resp.xpath("//ul[@class='sction-point-item']")
        for p in points:
            parents=points.xpath("./ancestor-or-self::ul[@class='chapter-item']")

