import main_function
import requests
import sear
import time

requests.packages.urllib3.disable_warnings()


# 对指定网站进行请求获取其网页源代码
print("******************************************")
print("***********网页源代码信息扫描器v1.0***********")
print("******************************************")
print("请将您所需要爬取网站的url，放入文本文件当中，命名为read.txt放在此目录下（支持批量检测）")

f = open('read.txt', encoding='utf-8')
txt = []
for line in f:
    txt.append(line.strip())
print("我们将对下面的网站开始爬取:")
for i in txt:
    print(i)
print("请确认。20秒后我们将开始执行脚本")
time.sleep(20)

for url in txt:
    get = main_function.Ping(url=url)  # 拿到网页源代码
    print(get)
    geturl = sear.SearchEveryUrl(get)  # 对于网页源代码当中url的筛选(初次)
    geturl.insert(0,url) # 将输入的网站也添加到检测当中，因为第一代网站更加重要
    path = sear.SearchPath(get)
    option = input("是否需要进行深度扫描(N/y)：")
    for i in geturl:
        try:
            sear.SearchGovern(i) # 判断是否为政府网站，是的话主动抛出异常
            geturl1 = main_function.Ping(i)  # 对指定网站发起请求，拿到网页源代码
        except:
            i = "error"
        else:
            path1 = sear.SearchPath(geturl1) # 对于path内容的搜索
            geturl2 = sear.SearchEveryUrl(geturl1) # 更加详细的url搜索
            pa = sear.SearchOtherPa(geturl1) # 对于路径的搜索
            path1.extend(geturl2) # 增加列表元素
            path1.extend(pa)
            if option == "N"or"n":
                break
    for k in path1:
        main_function.Savefile(filename="demo.txt", content=k, head=i)