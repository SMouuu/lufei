import asyncio
import aiofiles

import aiohttp

'''
"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fup.enterdesk.com%2Fedpic%2F4d%2Fd6%2Ff0%2F4dd6f0e142a057fba0bf73235c4167a5.jpg&refer=http%3A%2F%2Fup.enterdesk.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644222050&t=6d93def90690aeebccfae925fed7372f"
"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202006%2F01%2F20200601091140_yNxua.thumb.400_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644222084&t=012e25cb6d3e26378afaea3011a01188"
"https://img1.baidu.com/it/u=2476943548,3374522247&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400"
"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fitem%2F201601%2F10%2F20160110115717_3nEAS.jpeg&refer=http%3A%2F%2Fcdn.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644222120&t=4a46eba189a094a9de8afb656853f622"
'''


async def download(url):
    print("开始下载" + url)
    file_name = url.split("=")[-1] + ".jpg"
    #
    async with aiohttp.ClientSession() as session:
        # 发送网络请求
        async with session.get(url) as resp:
            # await resp.text()
            content = await resp.content.read()  # 相当于原来的 resp.content
            # 写入文件
            async with aiofiles.open(file_name, mode="wb") as f:
                await f.write(content)
    print("下载结束" + url)


async def main():
    url_list = [
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fup.enterdesk.com%2Fedpic%2F4d%2Fd6%2Ff0%2F4dd6f0e142a057fba0bf73235c4167a5.jpg&refer=http%3A%2F%2Fup.enterdesk.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644222050&t=6d93def90690aeebccfae925fed7372f",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202006%2F01%2F20200601091140_yNxua.thumb.400_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644222084&t=012e25cb6d3e26378afaea3011a01188",
        "https://img1.baidu.com/it/u=2476943548,3374522247&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fitem%2F201601%2F10%2F20160110115717_3nEAS.jpeg&refer=http%3A%2F%2Fcdn.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644222120&t=4a46eba189a094a9de8afb656853f622",

    ]
    tasks = []
    for url in url_list:
        t = asyncio.create_task(download(url))
        tasks.append(t)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
