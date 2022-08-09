import requests 
import os

url = 'https://www.obzhi.com/wp-content/uploads/2022/02/yuanshenquanjiafu2-scaled.jpg'
root = "E:\桌面\python\pic"
path = root + "元神.jpg"
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url, headers=headers)
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()

            print("文件保存成功")

    else:
        print('文件已存在')

except ConnectionError as err:
    print(err)