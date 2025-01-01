import requests
from bs4 import BeautifulSoup

# 百度首页网址
url = 'https://www.baidu.com'

# 发送GET请求
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 百度首页的标题通常在<title>标签中
    title = soup.find('h1').get_text()
    
    # 打印标题
    print('百度首页标题:', title)
else:
    print('请求失败，状态码:', response.status_code)