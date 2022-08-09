import requests
query = input('请输入你喜欢的一个明星：')

url = f'https://www.sogou.com/web?query={query}]'



dic ={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}

resp = requests.get(url,headers=dic)

print(resp)
print(resp.text)
resp.close()