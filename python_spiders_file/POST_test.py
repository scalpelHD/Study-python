import urllib.request
import urllib.parse


url = 'http:/www.iqianyue.com/mypost'
# 将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
postdata = urllib.parse.urlencode({
    'name': 'ceo@iqianyue.com',
    'pass': 'aA123456'}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("D:/spiders/HTNL/seven.html", 'wb')
fhandle.write(data)
fhandle.close()
