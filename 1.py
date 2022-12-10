import re

test = input("输入东西：")
rex = '.*?gov\.cn'
response = re.match(rex, test)
if response:
    print("我们发现了政府网站，准备抛出异常")
    raise RuntimeError('政府网站--Error')