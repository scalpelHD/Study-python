import re
import urllib.request


# 爬取CSDN首页上所有的链接
def getlink(url):
    """模拟成浏览器"""
    headers = ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/71.0.3554.0 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建正则表达式
    pat = '(https?://[^\s";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    # 去除重复元素
    link = list(set(link))
    return link


# 要爬取的网页链接
url = "http://blog.csdn.net/"
# 获取对应网页中包含的链接地址
linklist = getlink(url)
# 输出
for link in linklist:
    print(link[0])