# 下载国家地理杂志美图
#第一步先分析网页
#找到图片位置

from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"

#使用beautifulsoup找到带有 img_list 的这种 <ul>
html = requests.get(URL).text
soup = BeautifulSoup(html,'lxml')
img_ul = soup.find_all('ul',{"class":"img_list"})

#开始爬取
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
