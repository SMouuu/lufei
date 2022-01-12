import scrapy
from tupianzhijia.items import MeinvItem

class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['tupianzj.com']
    start_urls = ['https://www.tupianzj.com/bizhi/DNmeinv/']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="container"]/div/div/div[3]/div/ul/li')
        for li in li_list:
            href = li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url=response.urljoin(href),  # 把response中的url与子url进行拼接
                method='get',
                callback=self.parse_detail  # 回调函数
            )
            break

    def parse_detail(self, response, **kwargs):
        name=response.xpath('//*[@id="container"]/div/div/div[2]/h1').extract_first()
        img_src=response.xpath("//div[@id='bigpic']/a/img/@src").extract_first()
        meinvitem=MeinvItem()
        meinvitem['name']=name
        meinvitem['img_src']=img_src
        yield meinvitem

