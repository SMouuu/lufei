import requests

resp = requests.get(url="http://192.168.75.128:8050/render.html", params={
    "url": "https://bbs.tianya.cn/",
    "wait": 3
})

print(resp.text)
