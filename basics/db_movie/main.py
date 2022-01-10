import requests
import re
import asyncio
import aiofiles
import aiohttp
from lxml import etree
from urllib import parse


def get_page_source(url):
    resp = requests.get(url)
    return resp.text


def get_iframe_src(url):
    print("获取iframe的src值")
    page_source = get_page_source(url)
    tree = etree.HTML(page_source)
    src = tree.xpath("//iframe/@src")[0]
    src_url = parse.urljoin(url, src)
    print("成功获取iframe的src值")
    return src_url

def get_first_m3u8_url(src_url):
    print("获取第一层m3u8地址")
    page_source=get_page_source(src_url)
    obj=re.compile(r'url: "(?P<m3u8_url>.*?)",',re.S)
    result=obj.search(page_source)
    m3u8_url=result.group("m3u8_url")
    print("成功获取第一层m3u8地址")
    return m3u8_url

def download_m3u8_file(first_m3u8_url):
    print("下载m3u8文件内容")
    first_m3u8=get_page_source(first_m3u8_url)
    second_m3u8_url=first_m3u8.split()[-1]
    second_m3u8_url=parse.urljoin(first_m3u8_url,second_m3u8_url)
    print("成功下载m3u8文件内容")
    second_m3u8=get_page_source(second_m3u8_url)
    with open("second_m3u8.txt",mode='w',encoding='utf-8') as f:
        f.write(second_m3u8)
    print("成功写入m3u8文件内容")

async def download_one(url):
    #自省
    for i in range(10):
        try:
            file_name=url.split("/")[-1]
            # file_name=file_name.strip('\n')
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    content=await resp.content.read()
                    async with aiofiles.open(f"./电影_源_加密后/{file_name}",mode='wb')as f:
                        await f.write(content)
            print(url,"下载成功")
            break
        except:
            print("下载失败，出现错误",url)
            asyncio.sleep((i+1)*5) #可以适当的进行睡眠


async def download_all_ts():
    tasks=[]
    with open("second_m3u8.txt",mode='r',encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line=line.strip()
            task=asyncio.create_task(download_one(line))
            tasks.append(task)
    await asyncio.wait(tasks)

def get_key():
    # with open("second_m3u8.txt",mode='r',encoding='utf-8') as f:
    pass




def main():
    url = "http://www.wbdy.tv/play/30288_2_1.html"
    src_url = get_iframe_src(url)
    first_m3u8_url=get_first_m3u8_url(src_url)
    download_m3u8_file(first_m3u8_url)
    asyncio.run(download_all_ts())
    # loop=asyncio.get_event_loop()
    # loop.run_until_complete()


if __name__ == '__main__':
    main()
