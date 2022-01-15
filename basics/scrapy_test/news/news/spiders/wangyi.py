import scrapy
from scrapy_splash import SplashRequest
from scrapy_redis.spiders import RedisSpider
lua_source = '''
    function main(splash, args)
        assert (splash:go(args.url))
        assert (splash:wait(1))
        -- 加载一段js, 后面作为lua函数进行调用.
        -- 在这个脚本中, 主要返回"加载更多"按钮的状态
        get_display_style = splash:jsfunc([[
            function(){
                return document.getElementsByClassName('load_more_btn')[0].style.display;
        }
        ]])
        -- lua中的循环语句.和python的while功能一样.
        while (true)
            do -- 语法规定.相当于开始
                -- 直接运行js代码, 滚动到'加载更多'按钮
                splash: runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
                -- 等待
                splash: wait(1)
                -- 找到该按钮.点击它
                splash: select(".load_more_btn").click()
                -- 调用上方预制的js脚本, 获取'正在加载按钮'的状态
                display_style = get_display_style()
                -- 如果不显示了.也就结束了
                if (display_style == 'none')
                    then
                break
                -- 同python中的break.打断循环
                end
            end
            assert (splash:wait(2)) -- 不在乎多等2秒
            return {
                html = splash:html(),    -- 拿到页面源代码
                cookies = splash:get_cookies()  -- 拿到cookies
            }
    end
'''


class WangyiSpider(RedisSpider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    # start_urls = ['https://news.163.com/']
    redis_key = "wangyi:news:start_urls"

    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint="execute",  # 表示你要执行splash哪个服务
            args={
                "lua_source": lua_source,
                "wait":2
            },
            dont_filter=True
        )

    def parse(self, resp, **kwargs):
        divs = resp.xpath("//ul[@class='newsdata_list fixed_bar_padding noloading']/li[1]/div[2]/div")
        for div in divs:
            a = div.xpath("./div/div/h3/a")
            if not a:
                continue
            href = a.xpath('./@href').extract_first()
            title = a.xpath('./text()').extract_first()
            print(href)
            # 可以采用正常的抓取方案
            yield scrapy.Request(
                url=href,
                callback=self.details
            )
            break


    def details(self, resp):
        with open("data.txt", mode='w') as f:
            f.write("____".join(resp.xpath("//div[@class='post_body']//p/text()").extract()))
