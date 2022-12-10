import re


def SearchUrl(context):  # 对于网站url的筛选
    ex = '(https?://.*?(?:\.html|\.css|\.js|\.action|\.do|\.json))'  # 对于网站类型的查找
    response = re.findall(ex, context)
    return response


def SearchPhone(content):
    phone = "^1(3[0-9]|5[0-3,5-9]|7[1-3,5-8]|8[0-9])\d{8}$"  # 对于电话号码的查找
    response = re.findall(phone, content)
    return response


def SearchEmail(content):
    email = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'  # 对于邮箱的查找
    response = re.findall(email, content)
    return response


def SearchPath(content):  # 对于路径的筛选
    path = 'path:"(.*?)"'
    response = re.findall(path, content)
    return response


def SearchHref(content):
    href = 'href="(.*?)"'
    response = re.findall(href, content)
    return response


def SearchSrc(content):
    src = 'src="(.*?)"'
    response = re.findall(src, content)
    return response


def SearchEveryUrl(content):  # 更加强大的筛选
    path = '(https?://.*?)["|\>]'
    response = re.findall(path, content)
    return response


def SearchOtherPa(content):
    path = '"/.*?/.*?"'  # 一级
    path2 = '"/.*?/.*?/.*?"'  # 二级
    path3 = '"/.*?/.*?/.*?/.*?"'  # 三级
    path4 = '"/.*?/.*?/.*?/.*?/.*?"'  # 四级
    path5 = '"/.*?/.*?/.*?/.*?/.*?/.*?"'  # 五级
    path6 = '"/.*?/.*?/.*?/.*?/.*?/.*?/.*?"'  # 六级
    list = [path, path2, path3, path4, path5, path6]
    for i in list:
        demo_list = re.findall(i, content)
        demo_list.extend(demo_list)
    return demo_list


def SearchGovern(url):
    rex = '.*?gov\.cn'
    response = re.match(rex, url)
    if response:
        print("我们发现了政府网站，准备抛出异常")
        raise RuntimeError('政府网站--Error')
