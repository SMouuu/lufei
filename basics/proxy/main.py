import requests


# 第三方代理接入
def get_ip():
    url = ""
    resp = requests.get(url)
    ips = resp.json()
    for ip in ips['data']['proxy_list']:
        yield ip


def spider():
    url = "https://wwww.baidu.com"
    while 1:
        try:
            proxy_ip = next(gen)
            proxy = {
                "http": "http://" + proxy_ip,
                "https": "https://" + proxy_ip,
            }
            resp = requests.get(url, proxies=proxy)
            resp.encoding = 'utf-8'
            return resp.text
        except:
            print("代理可能失效")


if __name__ == '__main__':
    gen = get_ip()
    spider()
