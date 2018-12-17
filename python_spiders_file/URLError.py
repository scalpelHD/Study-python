# 处理爬取异常
import urllib.error
import urllib.request


try:
    urllib.request.urlopen('http://www.doutula.com')
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)