import scrapy


class XiaoSpider(scrapy.Spider):
    name = 'xiao'
    allowed_domains = ['4399.com']
    start_urls = ['http://www.4399.com/flash/']

    def parse(self, response):
        # 提取所有的数据
        # txt=response.xpath("//ul[@class='n-game cf']/li/a/b/text()").extract()
        # print(txt)

        # 分段提取数据
        li_list = response.xpath("//ul[@class='n-game cf']/li")
        for li in li_list:
            name = li.xpath("./a/b/text()").extract_first()
            categroy = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em/text()").extract_first()

            dic = {
                "name": name,
                "categroy": categroy,
                "date": date
            }
            yield dic
