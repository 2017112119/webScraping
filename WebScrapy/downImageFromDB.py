#爬取豆瓣新书速递，图片

#导入库
from bs4 import BeautifulSoup
import requests

#web page site
URL = 'https://book.douban.com/latest?icn=index-latestbook-all'

html = requests.get(URL).text
# print(html)
soup = BeautifulSoup(html,features='lxml') #网页解析
img_url = soup.find_all('a',{"class":"cover"})

# print(img_url)
#开始爬取
for ul in img_url:
    imgs = ul.find_all('img')  #得到图片链接
    for img in imgs:
        url = img['src']
        r = requests.get(url,stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
