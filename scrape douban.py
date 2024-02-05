 # 获取豆瓣前250个电影列表

import requests
#定义请求头，把爬虫程序伪装成用户浏览器请求

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
}

response = requests.get("https://movie.douban.com/top250", headers = header)

print(response.status_code)
print(response.text)