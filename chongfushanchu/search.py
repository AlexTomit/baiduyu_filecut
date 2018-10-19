import requests
from urllib.parse import quote
import json
#查询该文件夹下的文件列表，并返回
def get_file(path,cookies):
    url = "https://pan.baidu.com/api/list?dir="
    path = quote(path, safe='')
    url = url + path
    headers = {
        'Host': "pan.baidu.com",
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'Accept': "*/*",
        'Referer': "https://pan.baidu.com/disk/home?",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie':cookies,
       'cache-control': "no-cache",
       }

    response = requests.request("GET", url, headers=headers)
    c = json.loads(response.text)
    return c['list']
