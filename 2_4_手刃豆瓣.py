#拿到源代码   requests
#通过re来提取想要的有效信息   re

import requests
import re
import csv

url = "https://movie.douban.com/top250?start=25&filter="
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}
resp = requests.get(url,headers=headers)
page_content = resp.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<span class="title">&nbsp;/&nbsp;(?P<OriginalTitle>.*?)</span>.*?<span class="playable">(?P<playability>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<number>.*?)人评价</span>',re.S)

result = obj.finditer(page_content)
f = open('data.csv', mode='w', encoding="utf-8")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group('name'))
    # print(it.group('OriginalTitle'))
    # print(it.group('playability'))
    # print(it.group('year').strip())
    # print(it.group('score'))
    # print(it.group('number'))
    dic = it.groupdict()
    dic['year'] =dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print('over!')
resp.close()