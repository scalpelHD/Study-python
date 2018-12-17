import urllib.request
# 使用GET方式爬取网页

keyword = input('please input the keyword you want to research:')
keyword = urllib.request.quote(keyword)
url = 'https://www.baidu.com/s?ie=UTF-8&wd='+keyword
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/71.0.3554.0 Safari/537.36"}
req = urllib.request.Request(url, headers=headers)
data = urllib.request.urlopen(req).read()
fhandle = open('D:/spiders/HTML/sixx.html', 'wb')
fhandle.write(data)
fhandle.close()