import requests 
from bs4 import BeautifulSoup
from lxml import etree

url = "http://myhome.dangdang.com/myOrder"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
    "Cookie": "__ozlvd=1652774185; _jzqco=%7C%7C%7C%7C%7C1.1253290257.1652774946606.1652774946606.1652774946607.1652774946606.1652774946607.0.0.0.1.1; __permanent_id=20220518155651576350060173250813206; cart_items_count=33; cart_id=3000102300520400068; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; login_dang_code=20220524103945352100300457833241; USERNUM=vUNQRccZH27O/iIPTW4HJA==; login.dangdang.com=.AYH=&.ASPXAUTH=doq79twOWD5+vC2w1UgxwY6xsy4po/DHtPqJcCbqmity2zL+A/Hlwg==; dangdang.com=email=MTMxNDY3OTEwNTUyMTE4MEBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=7331650864947&customerid=BeO+wXFIEkE7vrnCUtvQ0w==&viptype=daczNiC4sWQ=&show_name=131%2A%2A%2A%2A1055; ddoy=email=1314679105521180%40ddmobilphone__user.com&nickname=&validatedflag=2&uname=1314679105521180%40ddmobilphone__user.com&utype=0&.ALFG=off&.ALTM=1653359991; sessionID=pc_4d3a5b997f09061c38b66dc30b1d75735a24d09676fdfa88b7b283303aa8e8ed; LOGIN_TIME=1653363436565; __rpm=...1653363435768%7C...1653363479574"
}

resp = requests.get(url, headers=headers)
resp.encoding = "gb2312"

html = etree.HTML(resp.json())
# divs = html.xpath("/html/body/div[2]/div[3]/div[3]/div[1]/div/div[2]")
# for div in divs:
#     href = div.xpath("./*[@id="orderList"]/div[1]/div/div[2]/div[1]/ul/li/a/@href")
#     print(href)
    
    