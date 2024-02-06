 # 获取豆瓣前250个电影列表

import requests

#定义请求头，把爬虫程序伪装成用户浏览器请求
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
}
for start_num in range(0,250,25): #每一页只显示25个电影名，我们需要执行10页
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers = header)

    # print(response.status_code) #只有输出200 才是成功
    # print(response.text) # 看到html 中的所有文字，比较复杂

    # 利用 beautiful soup 来解析HTML内容，缩短人工成本

    from bs4 import BeautifulSoup
    html = response.text
    soup = BeautifulSoup(html, "html.parser") # parser 为解析器，用来解析复杂的html文本
    all_titles = soup.find_all("span", attrs={"class": "title"}) #找到标签为span 中，class参数= title 的所有值

    for title in all_titles:
        title_string = title.get_text()
        if "/" not in title_string: print(title_string) #去掉除了中文之外的电影别名
