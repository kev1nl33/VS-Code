# 1. 如何提取单个页面的数据
# 2. 上线程池，多个页面同时抓去
import requests 
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode = "w" , encoding = "utf-8", newline = "")
csvwrite = csv.writer(f)

def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[4]/div/div[2]/div[1]/div/table")[0]
    trs = table.xpath("./tr")
    # trs = table.xpath("./tr")[1:]
    # trs = table.xpath("./tr[position()>1]")
    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 有/时，对数据做简单的处理： \\ 或者 / 去掉
        txt = (item.replace("\\","").replace("/","") for item in txt)
        csvwrite.writerow(txt)
    print(url,"提取完毕！")
    

    resp.close()
if __name__ == "__main__":
    # for i in range(1,9949): # 效率及其低下
    #     download_one_page(f'http://ygzapm.com/web/dailyPrice?totalPageCount=9949&pageNow={i}&product=&typeCode=')

    # 创建线程池
    with ThreadPoolExecutor(500) as t:
        for i in range(1, 9949):
            # 把下载任务交给线程池
            t.submit(download_one_page,f'http://ygzapm.com/web/dailyPrice?totalPageCount=9949&pageNow={i}&product=&typeCode=')
    
    print("全部下载完毕！")
