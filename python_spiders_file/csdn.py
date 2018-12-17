import urllib.request
# 伪装成浏览器爬取网页

url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
req = urllib.request.Request(url)
# 使用add_header()修改报头
req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36")
# 超时设置即在urlopen()中加一个参数timeout
data = urllib.request.urlopen(req).read()
fhandle = open('D:/spiders/HTML/five.html', 'wb')
fhandle.write(data)
fhandle.close()