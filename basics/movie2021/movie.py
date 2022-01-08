import re

import requests

url = "https://dy2018.com"
resp = requests.get(url)
resp.encoding = "gbk"
# print(resp.text)
# 提取影片段
obj = re.compile(r"2021必看热片.*?<ul>(?P<html>.*?)</ul>", re.S)
result = obj.search(resp.text)
html = result.group("html")
# 提取内容
obj2 = re.compile(r"<li><a href='(?P<u>.*?)'")
result2 = obj2.finditer(html)
obj3 = re.compile(r'id="Zoom">.*?◎片　　名　(?P<name>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<dowurl>.*?)">',re.S)
for i in result2:
    childurl = url + i.group("u")
    childresp = requests.get(childurl)
    childresp.encoding = "gbk"
    endresult=obj3.search(childresp.text)
    print(endresult.group("name"),endresult.group("dowurl"))