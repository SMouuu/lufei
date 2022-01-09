from selenium.webdriver import Chrome


if __name__ == '__main__':
    web = Chrome()
    url = "http://www.lagou.com"
    web.get(url)
    print(web.title)
