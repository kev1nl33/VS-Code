# 原理： 通过第三方机器发送请求。
import requests

# 65.18.114.254:55443
proxies = {
    "https":"https://65.18.114.254:55443"
}

resp =  requests.get('http://www.baidu.com', proxies = proxies)
resp.encoding = 'utf-8'
print(resp.json.)

