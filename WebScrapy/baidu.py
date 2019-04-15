# <a target="_blank" href="/item/%E8%9C%98%E8%9B%9B/8135707" data-lemmaid="8135707">蜘蛛</a>
# <a target="_blank" href="/item/%E8%A0%95%E8%99%AB">蠕虫</a>
# <a target="_blank" href="/item/%E9%80%9A%E7%94%A8%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E">通用搜索引擎</a>
#分析发现 这些链接的共同之处是  以 /item/开头， 有些以/item/开头，却不是词条
# <a href="/item/史记·2016?fr=navbar" target="_blank">史记·2016</a>

#制作爬虫
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"] #his作备案 ，记录我们浏览过的网页

#打印出我们正在哪张网页上

for i in range(0,20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    print(i,soup.find('h1').get_text(),' url:',his[-1])


    #find valid urls
    sub_urls = soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")}) #匹配词条

    if len(sub_urls) !=0:
        his.append(random.sample(sub_urls,1)[0]['href']) #random.sample(list,n) 从list 中随机选取n个元素
    else:
        #no valid sub link found
        his.pop()  #list.pop()  列表元素删除,默认为 最后一个
# print(his)

