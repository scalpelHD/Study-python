import re
import urllib.request
import time
import urllib.error


# 模拟成浏览器
headers = ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/71.0.3554.0 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
urllist = []


# 使用代理服务器
def use_proxy(proxy_addr, url):
    """建立异常处理"""
    try:
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        # 若为URLError异常，延时10秒
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        # 若为Exception异常，延时1秒
        time.sleep(1)


# 获取所有文章链接
def geturllist(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        # 编码关键词
        keycode = urllib.request.quote(key)
        # 编码&page
        pagecode = urllib.request.quote('&page')
        # 循环爬取各页的文章链接
        for page in range(pagestart, pageend):
            """分别构建各页的url链接，每次循环构建一次"""
            url = "http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            # 用代理服务器爬取，防止被封杀IP
            data1 = use_proxy(proxy, url)
            # 构建正则表达式
            urllistpat = '<div class="text-box">.*?(http://.*?)"'
            # 获取每页的文章链接并添加到列表中
            urllist.append(re.compile(urllistpat, re.S).findall(data1))
        print("共获取到"+str(len(urllist))+"页。")
        print(data1)
        return urllist
    except urllib.error.URLError as e :
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
            # 若为URLError异常，延时10秒
            time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常，延时1秒
        time.sleep(1)


# 通过文章链接获取对应内容
def getcontent(urllist, proxy):
    i = 0
    # 设置本地文件中的HTML编码
    html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/
    xhtml1-transitional.dtd">
    <html1 xmlns="http://www.w3.ogr/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>微信文章页面</title>
    </head>
    <body>'''
    fh = open("D:/spiders/HTML/eleven.html", "wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    # 再次以追加方式打开文件，以写进对应文章内容
    fh = open("D:/spiders/HTML/eleven.html", "ab")
    # 此时URLlist为二维列表，第一维储存第几页，第二维储存第几个链接
    for i in range(0, len(urllist)):
        for j in range(0, len(urllist[i])):
            try:
                # 构建正确的URL
                url = urllist[i][j]
                url = url.replace("amp;", '')
                # 开始使用代理服务器爬取
                data = use_proxy(proxy, url)
                # 构建文章标题正则表达式
                titlepat  = '<title>(.*?)</title>'
                # 构建文章内容正则表达式
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                # 通过正则表达式找到标题并赋值给列表title
                title = re.compile(titlepat).findall(data)
                # 通过正则表达式找到内容并赋值给列表content
                content = re.compile(contentpat, re.S).findall(data)
                # 初始化标题和内容
                thistitle = '此次标题没有找到'
                thiscontent = '此次内容没有找到'
                # 检查是否找到标题并赋值
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thiscontent = content[0]
                # 将标题和文章内容汇总
                dataall = "<p>标题为："+thistitle+"</p><p>内容为："+thiscontent+"</p><br>"
                # 将标题和内容写入文件
                fh.write(dataall.encode('utf-8'))
                print('第'+str(i)+'个网页第'+str(j)+'次处理')
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)
                    # 若为URLError异常，延时10秒
                    time.sleep(10)
            except Exception as e:
                print("exception:" + str(e))
                # 若为Exception异常，延时1秒
                time.sleep(1)
    fh.close()
    html2 = '''</body>
    </html>'''
    fh = open('D:/spiders/HTML/eleven.html', 'ab')
    fh.write(html2.encode('utf-8'))
    fh.close()


# 设置关键词
key = '物联网'
# 设置代理服务器
pro = ['59.110.240.249:8080', '115.46.65.211:8123', '119.31.210.170:7777', '120.92.74.189:3128', '61.135.217.7:80',
       '101.37.79.125:3128', '118.190.95.35:9001', '171.37.162.116:8123', '121.17.160.63:808', '118.190.95.35:9001',
       '202.112.237.102:3128', '113.200.56.13:8010', '113.128.148.31:8118', '110.40.13.5:80', '112.91.218.21	:9000']
proxy = pro[0]
# proxy2 = '113.16.160.101:8118'
pagestart = 1
pageend = 2
urllist = geturllist(key, pagestart, pageend, proxy)
getcontent(urllist, proxy)
