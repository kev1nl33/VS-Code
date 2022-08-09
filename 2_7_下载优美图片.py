# 1.拿到主页面的源代码，然后提取子页面的链接地址：href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址  img -> src
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time


url = "https://umei.cc/bizhitupian/weimeibizhi/"

resp = requests.get(url)
resp.encoding = "utf-8" #处理乱码

# print(resp.text)
#把源代码交给bs
main_page = BeautifulSoup(resp.text,"html.parser")
a_list = main_page.find("ul", class_="pic-list after").find_all("a")
print(a_list)
for a in a_list:
    href = "https://www.umei.cc"+ a.get('href')#直接通过get就可以拿到属性的值
    # print(href)
    #拿到子页面源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    section = child_page.find("section",class_="img-content")
    img = section.find("img")
    src = img.get('src')
    #下载图片
    img_resp = requests.get(src)
    # img_resp.content #拿到的是字节
    img_name = src.split('/')[-1] #拿到url中的最后一个/以后的内容
    with open(img_name, mode = "wb") as f:
        f.write(img_resp.content) #图片内容写入文件

    print('over!!', img_name)
    time.sleep(1)

print('all over!!!')





resp.close()
