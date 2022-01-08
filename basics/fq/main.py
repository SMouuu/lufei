from pyquery import PyQuery

html='''
    <li><a href="http://www.baidu.com">百度</a></li>
'''

p=PyQuery(html)
li=p("li")
print(li)