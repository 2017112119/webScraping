#下载图片
#
import os
os.makedirs('./img/',exist_ok=True)
#图片地址
IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

#使用urlretrieve  下载功能
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'./img/image1.png')

#使用requests
import requests
r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)
# 如果你要下载的是大文件, 比如视频等. requests 能让你下一点, 保存一点,
# 而不是要全部下载完才能保存去另外的地方. 这就是一个 chunk 一个 chunk 的下载.
# 使用 r.iter_content(chunk_size) 来控制每个 chunk 的大小, 然后在文件中写入这个 chunk 大小的数据.
r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)

