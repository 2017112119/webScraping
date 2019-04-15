#导入 beautifulsoup  用于解析网页
from bs4 import BeautifulSoup
from urllib.request import urlopen

#If exists Chinese ,apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')#read the web content
print(html) #output the html content.

soup = BeautifulSoup(html,features='lxml')  #读取网页信息，以lxml 形式加载, soup 中装载着网页所有的信息
print(soup.h1)  #输出h1 标签
# <h1>爬虫测试1</h1>
print("\n",soup.p)
# <p>
# 		这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
# <a href="https://morvanzhou.github.io/tutorials/data-manipulation/scraping/">爬虫教程</a> 中的简单测试.
# 	</p>

#如果网页中有多个同样的tag,  可以使用 find_all() 来找到所有的选项
all_href = soup.find_all('a')  #找到所有的tag <a>
all_href = [l['href'] for l in all_href]   #索引得到其中的链接
print("\n",all_href)
# ['https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/data-manipulation/scraping/']
