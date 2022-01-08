import requests
import re

# 正则匹配豆瓣250数据
# 拿到页面源代码
# 编写正则，提取页面数据
# 保存数据

f = open("top250.csv", mode="w", encoding='utf-8')
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
}
resp = requests.get("https://movie.douban.com/top250", headers=headers)
pageSource = resp.text
# print(pageSource)
# re.S 可以让正则匹配换行符
obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?导演: (?P<dao>.*?)&nbsp;.*?<br>(?P<year>.*?)', re.S)
result = obj.finditer(pageSource)
for item in result:
    name=item.group("name")
    dao=item.group("dao")
    f.write(f"{name},{dao}\n")
f.close()
resp.close()
print("豆瓣top250提取完毕")