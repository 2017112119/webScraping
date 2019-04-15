#beautifulsoup解析网页  正则表达式

#正则匹配
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#if exist chinese ,apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
print(html)
#发现 图片 在 tag 中  td
soup = BeautifulSoup(html,features='lxml')

img_links = soup.find_all("img",{"src":re.compile('.*?\.jpg')})  #匹配图片
for link in img_links:
    print(link['src'])
# https://morvanzhou.github.io/static/img/course_cover/tf.jpg
# https://morvanzhou.github.io/static/img/course_cover/rl.jpg
# https://morvanzhou.github.io/static/img/course_cover/scraping.jpg

#匹配课程链接
course_links = soup.find_all('a',{'href':re.compile('https://morvan.*')})
for link in course_links:
    print(link['href'])
# https://morvanzhou.github.io/
# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/
# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/
# https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/
# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/
