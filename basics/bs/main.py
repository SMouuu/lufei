from bs4 import BeautifulSoup

html = '''
    <ul>
        <li><a href="zhangwuji.com">张无忌</a></li>
        <li id="abc"><a href="zhouxinchi.com">周星驰</a></li>
        <li><a href="zhubajie.com">猪八戒</a></li>
        <li><a href="wuzetian.com">武则天</a></li>
    </ul>
'''

html = BeautifulSoup(html, "html.parser")
li=html.find("li",attrs={"id":"abc"})
a=li.find("a")
print(a.text)
print(a.get("href"))
print(a)


