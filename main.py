import re
import main_function
import requests
import sear
import time

requests.packages.urllib3.disable_warnings()

# 对指定网站进行请求获取其网页源代码
print("******************************************")
print("***********网页源代码信息扫描器v2.0***********")
print("******************************************")
print("请将您所需要爬取网站的url，放入文本文件当中，命名为read.txt放在此目录下（支持批量检测）")

All_list = []
urls = []  # url
path = []  # 路径
annotation = []  # 注释
f = open('read.txt', encoding='utf-8')
txt = []
for line in f:
    txt.append(line.strip())
print("我们将对下面的网站开始爬取:")
for i in txt:
    print(i)
option = input("准备好了吗？")

for url in txt:
    get = main_function.Ping(url=url)  # 拿到网页源代码
    geturl = sear.SearchUrl(get)  # 对于网页源代码当中url的筛选(初次)
    geturl.insert(0, url)  # 将输入的网站也添加到检测当中，因为第一代网站更加重要
    path = sear.SearchPath(get)
    for i in geturl:
        try:
            sear.SearchGovern(i)  # 判断是否为政府网站，是的话主动抛出异常
            geturl1 = main_function.Ping(i)  # 对指定网站发起请求，拿到网页源代码
        except:
            i = "error"
        else:
            path1 = sear.SearchPath(geturl1)  # 对于path内容的搜索
            All_list.extend(path1)
            geturl2 = sear.SearchUrl(geturl1)  # 更加详细的url搜索
            All_list.extend(geturl2)
            pa = sear.SearchOtherPa(geturl1)  # 对于路径的搜索
            All_list.extend(pa)
            ann = sear.Searchann(geturl1)
            All_list.extend(ann)

            main_function.Savefile(filename='demo.txt', content="下面是对" + i + "网站的搜索结果")
            rex = 'https?\://'
            rex2 = '(<!-- .*? -->)'
            for k in All_list:
                if re.match(rex, k):
                    urls.append(k)
                elif re.match(rex2, k):
                    annotation.append(k)
                else:
                    path.append(k)

            main_function.Savefile(filename="demo.txt", content="url网址有:")
            for s in urls:
                main_function.Savefile(filename="demo.txt", content=s)

            main_function.Savefile(filename="demo.txt", content="路径有:")
            for o in path:
                main_function.Savefile(filename="demo.txt", content=o)

            All_list = []  # 释放变量
            urls = []  # url
            path = []  # 路径
            annotation = []  # 注释

print(
    "愿中国青年都摆脱冷气,只是向上走,不必听自暴自弃者流的话。能做事的做事,能发声的发声。有一分热,发一分光。就令萤火一般,也可以在黑暗里发一点光,不必等候炬火。")
