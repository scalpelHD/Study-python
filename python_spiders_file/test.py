import urllib.request
import urllib.parse

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LlKxw"
postdata = urllib.parse.urlencode({
    "username": "weisuen",
    "password": "aA123456"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/71.0.3554.0 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("D:/spiders/HTML/nine.html", "wb")
fhandle.write(data)
fhandle.close()
url2 = 'http://bbs.chinaunix.net/'
req2 = urllib.request.Request(url2, postdata)
req2.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/71.0.3554.0 Safari/537.36")
data2 = urllib.request.urlopen(req2).read()
fhandle = open("D:/spiders/HTML/ten.html", "wb")
fhandle.write(data)
fhandle.close()
