

import requests
from lxml import etree
import os

def main():
    if not os.path.exists("./pictures"):  # 创建文件夹
        os.mkdir("./pictures")
    url = "http://pic.netbian.com/"  # 图片网址
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}# 请求头信息
    for i in range(0,6):  # 获取前5页，如果想要爬取更多，直接更改后面的数字，（爬取较多需要加代{过}{滤}理ip）
        new_url = format(url%i)
        r = requests.get(url=new_url,headers=header)
        r.encoding = r.apparent_encoding
        page_text = r.text # 获取网页信息
        tree = etree.HTML(page_text)
        li_list = tree.xpath("//div[@class='slist']//li")  # 使用xpath解析网页
        for li in li_list:
            pic_src = "http://pic.netbian.com"+li.xpath("./a/img/@src")[0] # 解析图片的网址
            img_name = li.xpath("./a/img/@alt")[0]+".jpg" # 解析图片名称
            img_data = requests.get(url=pic_src,headers= header).content # 获取图片信息并保存为二进制格式
            img_path = "pictures/"+img_name  # 文件保存路径为上面创建的文件夹
            with open(img_path, "wb") as fp :
                fp.write(img_data)
            print(img_name,"爬取成功")
    print("over!!!")
if __name__ == "__main__":
    main()