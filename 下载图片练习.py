
from unicodedata import name
import requests
from bs4 import BeautifulSoup
import time
import os



url = "https://unsplash.com/"
resp = requests.get(url)
resp.encoding = 'utf-8'

main_page = BeautifulSoup(resp.text, "html.parser")
figure_list = main_page.find("div", class_="ripi6").find_all('figure')
for a in figure_list:
    div = a.find("div",class_="zmDAx")
    for b in div:
        href = b.get("href")
        href_all = 'https://unsplash.com'+ href
        # print(href_all) #子页面源代码

        sub_page_resp = requests.get(href_all)
        sub_page_resp.encoding = "utf-8"
        sub_page_text = sub_page_resp.text
        
        sub_page = BeautifulSoup(sub_page_text,"html.parser")
        div = sub_page.find("div",class_="i3cUy")
        img = div.find("img")
        src = img.get('src') # 获得图片链接
        print(src)

        img_resp = requests.get(src)
        img_name = src.split('/')[-1]
        with open( img_name, mode = "wb") as f:
            f.write(img_resp.content)
        
        print("over!", img_name)
        time.sleep(3)
print("all done!")



        










#     sub_page_resp = requests.get(href_all)
#     sub_page_resp.encoding = "utf-8"

# # 1.尝试从主页面源代码中直接获取下载链接
# src = img_list.find(class_="YVj9w")
# src_list = src.find('src')
# src_link = src.get('src')
# print(src_link)



resp.close()