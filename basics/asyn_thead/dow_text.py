import requests
import asyncio
import aiohttp
from lxml import etree
import aiofiles


# 扒光一部小说

def get_every_chapter_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",

    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    tree = etree.HTML(resp.text)
    href_list = tree.xpath("//div[@class='booklist clearfix']/span/a/@href")
    # print(href_list)
    return href_list


async def download_one(url):
    while 1:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    page_source = await resp.text()
                    tree = etree.HTML(page_source)
                    title = tree.xpath("//div[@class='chaptertitle clearfix']/h1/text()")[0].strip()
                    content = "\n".join(tree.xpath("//div[@id='BookText']/text()")).replace("\u3000", "")
                    async with aiofiles.open(f"./明朝那些事儿/{title}.txt", mode="w", encoding='utf-8') as f:
                        await f.write(content)
                    break
        except:
            print("报错了，重试"+url)
    print("下载完毕", url)


async def download(href_list):
    tasks = []
    for href in href_list:
        t = asyncio.create_task(download_one(href))
        tasks.append(t)
    await asyncio.wait(tasks)


def main():
    url = "https://www.zanghaihua.org/mingchaonaxieshier/"
    # 1.拿到页面当中每一个章节的url
    href_list = get_every_chapter_url(url)
    # 2.启动携程，开始一节一节的下载
    asyncio.run(download(href_list))


if __name__ == '__main__':
    main()
