import requests
import re
import urllib.request


# 爬取表情包
def craw(url, p):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/71.0.3554.0 Safari/537.36"}
    data = requests.get(url, headers=headers).text
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg, re.S)
    imagelist = re.findall(reg, data)
    x = 1
    for i in imagelist:
        imagename = "D:/spiders/biaoqingbao/"+"page"+str(p)+"_"+str(x)+i[1]+".jpg"
        try:
            urllib.request.urlretrieve(i[0], filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
                x += 1
            if hasattr(e, "reason"):
                print(e.reason)
                x += 1
        except OSError:
            x += 1
        x += 1


for p in range(1, 10):
    url = 'http://www.doutula.com/photo/list/?page='+str(p)
    craw(url, p)
