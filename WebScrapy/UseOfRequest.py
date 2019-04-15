#加载网页有几种类型 ，最重要的类型 就是 get 和 post

    # post
    #     账号登录
    #     搜索内容
    #     上传图片
    #     上传文件
    #     往服务器传数据 等
    # get
    #     正常打开网页
    #     不往服务器传数据

#get请求
import requests
import webbrowser  #控制浏览器
param = {"wd":"莫烦Python"} #搜索的信息
r = requests.get('http://www.baidu.com/s',params=param)
print(r.url)
# webbrowser.open(r.url) #打开网页
#https://www.baidu.com/s?wd=%E8%8E%AB%E7%83%A6Python

#post 请求
data = {'firstname':'莫烦','lastname':'周'}
r = requests.post('http://pythonscraping.com/files/processing.php',data=data)
print(r.text)

#图片上传
file = {'uploadFile': open('image.png', 'rb')}
r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(r.text)

# The file image.png has been uploaded.

#登录
payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

# Hey Morvan! Looks like you're still logged into the site!


#使用Session登录
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)

# Hey Morvan! Looks like you're still logged into the site!
