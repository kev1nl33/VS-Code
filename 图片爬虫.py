
# BS4爬去图片尝试

# import requests 
# from bs4 import BeautifulSoup

# url = "https://www.obzhi.com/category/youxibizhi"
# resp = requests.get(url)
# resp.encoding = "utf-8"

# main_page = BeautifulSoup(resp.text, "html.parser")
# a_list = main_page.find('li', class_ ="post box row fixed-hight").find('div',class_ ="thumbnail").find_all('a')
# for a in a_list:
#     href = a.get("href") 
#     # 拿到进入子页面代码
#     print(href)

#     # sub_page_resp = requests.get(href)
#     # sub_page_resp.encoding = "utf-8"
#     # sub_page_text = sub_page_resp.text
#     # #子页面解析准备工作完毕
#     # sub_page = BeautifulSoup(sub_page_text, "html.parser") #将子页面源代码交给bs
#     # context = sub_page.find("div", class_= "context")
#     # img = context.find('img')
#     # src = img.get('src')
#     # print(src)

#resp.close()

from lxml import etree
import requests
import time
import urllib.request
import os
import re

# base_url = ""
# base_dir = "E:/桌面/python/gamepic"
# def savePic(pic_rul):
#     if not os.path.exists(base_dir):
#         os.makedirs(base_dir)
#     arr = pic_url.split('/')
#     file_name = base_dir + arr[-2]+arr[-1]
#     print(file_name)
#     response = requests.get(pic_url)

#     with open('file_name', 'wb') as fp:
#         for data in response.iter_content(128):
#             fp.write(data)



parser = etree.HTMLParser(encoding="utf-8")
url = "https://www.obzhi.com/category/youxibizhi"
resp = requests.get(url)
html = etree.HTML(resp.text)
divs = html.xpath('/html/body/div[4]/div[3]/ul/li')
for div in divs:
    href = div.xpath('./div[1]/a/@href') #使用xpath获取子页面href
    for h in href:
        sub_page_resp = requests.get(h)
        sub_page_html = etree.HTML(sub_page_resp.text)
        # figure = html.xpath('/html/body/div[3]/div[3]/div[1]/div[3]/div[1]/figure')
        # name = sub_page_html.xpath('/html/body/div[3]/div[3]/div[1]/div[3]/div[1]/figure/a/@data-title/text()')
        src = sub_page_html.xpath('/html/body/div[3]/div[3]/div[1]/div[3]/div[1]/figure/a/img/@src')
        print(src)


        # with open( img_name, mode = "wb") as f:
        #     f.write(requests.get(src).content)
        #     f.close()

    # with open("file", "wb") as f:
    #     f.write(requests.get(src).content)

    # if src == []:
    #     break





resp.close()
