#爬虫:通过编写程序来获取互联网上的资源
#需求：用程序模拟浏览器，输入一个网址，从该网址中获取资源和内容
from urllib.request import urlopen

url = "https://www.zhihu.com/"
resp = urlopen(url)

with open('myzhihu.html', mode='w', encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")