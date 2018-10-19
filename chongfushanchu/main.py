from cut import *
from search import get_file
lie_biao = []
#迭代查询和删除函数
def test(s,cookies,bdstoken):
    #获取文件列表
    l = get_file(s,cookies)
    for i in l:
        try:
            # 判断是否是文件夹以便继续循环
            if i["isdir"] == 1:
                test(i["path"],cookies,bdstoken)
            else:
                #如果MD5值存在于liebiao中，删除、、否则将MD5加入liebiao
                if i["md5"] in lie_biao:
                    cut(i["path"],cookies,bdstoken)
                else:
                    lie_biao.append(i["md5"])
        except:
            pass
if __name__ == "__main__":
    #删除入口，首先浏览器获取自己的cookie和bdstoken，填入
    cookies = ""
    bdstoken = ""
    test("/",cookies,bdstoken)
    #cut_some(data,cookies,bdstoken)
    print("ok!")