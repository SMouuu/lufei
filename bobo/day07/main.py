import requests


url = 'https://www.sogou.com/'
res = requests.get(url=url)
print(res.text)

