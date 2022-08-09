# 1. 登陆 -> 得到cookie
# 2. 带着cookie 去请求到书架url -> 书架上的内容

# 必须得把上面两个操作连起来
# 我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中cookie不会丢失

import requests 

#会话 
# session = requests.session()
# data = {"loginName": "15201457237",
#     'password': "7539514682.lR"
# }

# # 1. 登陆
# url = "https://passport.17k.com/ck/user/login"
# session.post(url, data = data)
# # print(resp.text)
# # print(resp.cookies)
# # 2. 拿书架上的数据
# # 刚才的session中有cookie的
# resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
# print(resp.json())

# 从浏览器直接复制cookie用于跳过登陆
resp = requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919', headers ={
    "Cookie": "GUID=f0e15a2f-f635-4473-8604-38cce8bfacc2; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F12%252F72%252F19%252F96571972.jpg-88x88%253Fv%253D1652601635000%26id%3D96571972%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B009AUs5Z2%26e%3D1668153932%26s%3D7470ec088eb9bd9d"
} )
print(resp.text)