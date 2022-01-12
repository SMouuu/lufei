import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/user/88146276/get/new/msg?appKey=2406394919']

    # 直接从浏览器复制cookie信息
    # def start_requests(self):
    #     cookie_str=""
    #     lst=cookie_str.split("; ")
    #     dic={}
    #     for it in lst:
    #         k,v=it.split("=")
    #         dic[k.strip()]=v.strip()
    #     yield scrapy.Request(
    #         url=self.start_urls[0],
    #         headers="",
    #         cookies=dic
    #     )

    # 走登录流程

    def start_requests(self):
        url = "https://passport.17k.com/ck/user/login"
        username = "15000187941"
        password = "sjhaoshuai123"
        yield scrapy.FormRequest(
            url=url,
            formdata={
                "loginName": username,
                "password": password
            },
            callback=self.parse
        )

    def parse(self, response):
        yield scrapy.Request(url=LoginSpider.start_urls[0], callback=self.parse_detail)

    def parse_detail(self, resp):
        print(resp.text)
