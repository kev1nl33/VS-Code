    #安装
#pip install bs4 -i 清华

# 1. 拿到页面源代码
# 2. 使用bs4进行解析，拿到数据

import requests
from bs4 import BeautifulSoup

url = 'https://www.guo68.com/market'
response = requests.get(url)

# 解析数据
# 1. 把页面源代码交给beautifulSoup进行处理，生成bs对象
page = BeautifulSoup(response.text,"html.parser") #指定html解析器
# 2. 从bs对象中查找数据
# find（标签，属性=值）
# find_all（标签，属性=值）
# page.find("table",class_="hq_table") # class是python里的关键字，id可能也是
# class_ 是在bs4里与python的class做区分。
table = page.find("li class",attrs={'class':'list1'})  # attrs= 与_class效果一样，喜欢用哪个用哪个

print(table)
# 拿到所有数据行，tr = table row,td = table data 
trs = table.find_all("tr")[1:]
for tr in trs: # 每一行
    tr.find_all("td") # 每行中的所有td
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容
    tds[0].text # .text表示拿到被标签标记的内容



