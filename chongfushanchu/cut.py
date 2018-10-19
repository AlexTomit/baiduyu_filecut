import requests
from urllib.parse import quote
import json
#删除主函数
def cut(a,cookies,bdstoken):
    t = ""
    for s in range(len(a)):
        if a[s]!="\\" or a[s+1]!='/':
            t=t+a[s]
    t = '["' + t + '"]'
    url = "https://pan.baidu.com/api/filemanager"
    querystring = {"opera":"delete","bdstoken":bdstoken}
    payload = "filelist=" + quote(t,safe='')
    headers = {
        'Host': "pan.baidu.com",
        'Connection': "close",
        'Content-Length': "122",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "https://pan.baidu.com",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Referer': "https://pan.baidu.com/disk/home?",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie':cookies,
         'cache-control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response.text

#以列表形式删除（比如有空文件夹列表，直接删除）
def cut_some(data,cookies,bdstoken):
    data = json.dumps(data)
    c = json.loads(data)
    d = 0
    for i in c:
        cut(i["path"],cookies,bdstoken)
        d+=1
    print(d)


