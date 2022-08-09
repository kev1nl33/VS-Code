#定位到2022必看片
#从2022必看片提取子页面链接店址
#请求子页面链接地址，拿到我们想要的下载地址。
import requests
import re

domain = "https://www.dytt89.com/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}
resp = requests.get(domain,headers=headers)
resp.encoding = 'gb2312' # 指定字符集

#拿到ul里的li
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')

    #提取到子页面链接:
    result2 = obj2.finditer(ul)
    for itt in result2:
        #拼接子页面rul地址：域名+子页面地址
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)

# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href,headers=headers)
    child_resp.encoding = "gb2312"
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))

resp.close()