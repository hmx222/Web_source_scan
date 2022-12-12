import requests


def Ping(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
               'referer': 'https://www.baidu.com', "Connection": "close"}
    response = requests.get(url=url, headers=headers, timeout=8, verify=False).text  # 对于输入网站的请求
    return response


def Savefile(filename, content):
    try:
        f = open(filename, "x", encoding='utf-8')  # 先打开一个文件
    except:
        f = open(filename, 'a', encoding='utf-8')
        f.write(content + "\n\n")
        f.close()
    else:
        print("我们将新建一个文件：%s" % filename)
        f.write(content + "\n\n")
        f.close()

