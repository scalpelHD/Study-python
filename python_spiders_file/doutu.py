import urllib.request
# 伪装成浏览器爬取网页

url = 'http://www.doutula.com/'
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/71.0.3554.0 Safari/537.36")
# 使用bulid_opener()修改报头
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open("D:/spiders/HTML/four.html", 'wb')
fhandle.write(data)
fhandle.close()