# 使用代理IP并伪装成浏览器爬取网页
import urllib.request


def use_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/71.0.3554.0 Safari/537.36")
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = opener.open(url).read()
    return data


proxy_addr = "119.31.210.170:7777"
try:
    data = use_proxy(proxy_addr, 'http://www.doutula.com/')
except urllib.request.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
else:
    fhandle = open("D:/spiders/HTML/et.html", 'wb')
    fhandle.write(data)
    fhandle.close()

