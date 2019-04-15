#beautifulsoup 解析 网页：css

#css 可以让网页变得丰富多彩 ，文字有了颜色，字体，位置也多样了
#css  用来装饰网页

from bs4 import BeautifulSoup
from urllib.request import urlopen

#if exist chinese ,apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)#打印网页源码

#按class匹配
soup = BeautifulSoup(html,features='lxml')  #解析网页

month = soup.find_all('li',{'class':'month'})
for m in month:
    print(m.get_text())
# 一月
# 二月
# 三月
# 四月
# 五月

jan = soup.find('ul',{"class":'jan'})
d_jan = jan.find_all('li')   #use jan as a parent
for d in d_jan:
    print(d.get_text())
# 一月一号
# 一月二号
# 一月三号
