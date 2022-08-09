import requests
import re

url = "https://movie.douban.com/top250"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}
resp = requests.get(url=url,headers=headers)
s = resp.text

obj = re.compile(r'</div>.*?<span class="title">(?P<name>.*?)</span>.*?</div>.*?<span class="inq">(?P<sentence>.*?)</span>',re.S)

result = obj.finditer(s)
for it in result:
    name = (it.group('name'))
    sentence = (it.group('sentence'))
    print(name,":", sentence)


    resp.close()
