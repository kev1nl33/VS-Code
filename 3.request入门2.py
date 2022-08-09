import requests

url = 'https://fanyi.baidu.com/sug'

s= input("请输入您要翻译的英文单词:")
dat ={
    "kw": s
}

resp = requests.post(url,data=dat)
print(resp.json()) #将服务器返回的内容直接处理成json