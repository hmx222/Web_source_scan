
import requests
import sear

requests.packages.urllib3.disable_warnings()


# 对指定网站进行请求获取其网页源代码
def Ping(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
               'referer': 'https://www.baidu.com', "Connection": "close"}
    response = requests.get(url=url, headers=headers,timeout=8).text  # 对于输入网站的请求
    return response


def Savefile(filename, content, head):  # 这里的head为url网站
    try:
        f = open(filename, "x", encoding='utf-8')  # 先打开一个文件
    except:
        # print("我们发现了一个您已经新建的文件：%s" % filename)
        f = open(filename, 'a', encoding='utf-8')
        f.write(head + "\n" + content + "\n\n")
        f.close()
    else:
        print("我们将新建一个文件：%s" % filename)
        f.write(head + "\n" + content + "\n\n")
        f.close()
    print("文件写入完毕")


print("******************************************")
print("***********网页源代码信息扫描器v1.0***********")
print("******************************************")
url = str(input("请输入网站："))
get = Ping(url=url)  # 拿到网页源代码
geturl = sear.SearchEveryUrl(get)  # 对于网页源代码当中url的筛选(初次)
geturl.insert(0,url) # 将输入的网站也添加到检测当中，因为第一代网站更加重要
path = sear.SearchPath(get)
option = input("是否需要进行深度扫描(N/y)：")


for i in geturl:
    try:
        sear.SearchGovern(i) # 判断是否为政府网站，是的话主动抛出异常
        geturl1 = Ping(i)  # 对指定网站发起请求，拿到网页源代码
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
    Savefile(filename="demo.txt", content=k, head=i)
