#use python to login web page.
#导入库
from urllib.request import urlopen

#if exist chinese apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')   #网页读取
#输出网页内容
print(html)

#match web page content
#导入正则匹配库
import re
res = re.findall(r"<title>(.+?)</title>",html)  #match the title
print("\nPage title is:",res[0])
# Page title is: Scraping tutorial 1 | 莫烦Python

res = re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)   #我们给一个 flags=re.DOTALL 来对这些 tab, new line 不敏感
print("\nPage paragraph is:",res[0])
# Page paragraph is:
# 		这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
# 		<a href="https://morvanzhou.github.io/tutorials/data-manipulation/scraping/">爬虫教程</a> 中的简单测试.

#找到网页中所有的链接
res = re.findall(r'href="(.*?)"',html)
print(res)
# ['https://morvanzhou.github.io/static/img/description/tab_icon.png', 'https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/data-manipulation/scraping/']
