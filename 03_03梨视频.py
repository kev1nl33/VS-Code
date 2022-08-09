# 1. 拿到contID
# 2. 拿到videostatus返回的json -> srcURL
# 3. srcURL里面的内容进行修正
# 4. 下载视频

import requests

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1762160"
contID = url.split('_')[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.856171327225947" 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
    # 防盗链 ： 溯源，当前请求的上一级是谁
    "Referer": "https://www.pearvideo.com/video_1762160"
}
resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]['srcUrl']
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")

# 下载视频
with open("b", mode = "wb") as f:
    f.write(requests.get(srcUrl).content)

print("well done!")