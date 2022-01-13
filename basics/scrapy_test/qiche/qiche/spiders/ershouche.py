import scrapy
from scrapy.linkextractors import LinkExtractor


class ErshoucheSpider(scrapy.Spider):
    name = 'ershouche'
    allowed_domains = ['che168.com', 'autohome.com.cn']
    start_urls = ['https://www.che168.com/china/list/#pvareaid=100945']

    def parse(self, response, **kwargs):
        # hrefs = response.xpath("//ul[@class='viewlist_ul']/li/a/@href").extract()
        # for h in hrefs:
        #     yield scrapy.Request(
        #         url=response.urljoin(h),
        #         callback=self.parse_detail
        #     )
        # scrapy的链接提取器
        le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a",))
        links = le.extract_links(response)
        for link in links:
            print(link.text.replace(" ","").strip(), link.url)
            yield scrapy.Request(
                url=link.url,
                callback=self.parse_detail
            )

        #开始分页
        page_le=LinkExtractor(restrict_xpaths=("//div[@id='listpagination']/a",))
        page_links=page_le.extract_links(response)
        for page_link in page_links:
            yield scrapy.Request(
                url=page_link.url,
                # dont_filter=True, 不过滤请求
                callback=self.parse
            )






    def parse_detail(self, resp, **kwargs):
        print(resp.url)
