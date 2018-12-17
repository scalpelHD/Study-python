import re
import queue
import urllib.request
import time
import threading
import urllib.error


urllist = []
urlqueue = queue.Queue()
headers = ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/71.0.3554.0 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
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


# 线程1，专门获取对应网址并处理成真实网址
class geturl(threading.Thread):
    def __init__(self, key, pagestart, pageend, proxy, urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue = queue
        self.key = key
    def run(self):
        page = self.pagestart
        key = self.key
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote('&page')
        for page in range(self.pagestart, self.pageend+1):
            """分别构建各页的url链接，每次循环构建一次"""
            url = "http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            # 用代理服务器爬取，防止被封杀IP
            data1 = use_proxy(self.proxy, url)
            # 构建正则表达式
            urllistpat = '<div class="text-box">.*?(http://.*?)"'
            # 获取每页的文章链接并添加到列表中
            urllist.append(re.compile(urllistpat, re.S).findall(data1))
        print("共获取到"+str(len(urllist))+"页。")
        for i in range(0, len(urllist)):
            """等一等线程1"""
            time.sleep(7)
            for j in range(0, len(urllist[i])):
                try:
                    url = urllist[i][j]
                    url = url.replace("amp;", "")
                    print('第'+str(i)+"i"+str(j)+"j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
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


# 线程2，与线程1并行执行。从线程1提供的文章网址中依次爬取对应文章信息并处理
class getcontent(threading.Thread):
    def __init__(self, urlqueue, proxy):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy
    def run(self):
        html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/
    xhtml1-transitional.dtd">
    <html1 xmlns="http://www.w3.ogr/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>微信文章页面</title>
    </head>
    <body>'''
        fh = open("D:/spiders/HTML/hd.html", 'wb')
        fh.write(html1.encode('utf-8'))
        fh.close()
        fh = open("D:/spiders/HTML/hd.html", 'ab')
        i = 1
        while(True):
            try:
                url = self.urlqueue.get()
                data = use_proxy(self.proxy, url)
                titlepat = '<title>(.*?)</title>'
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
                dataall = "<p>标题为：" + thistitle + "</p><p>内容为：" + thiscontent + "</p><br>"
                # 将标题和内容写入文件
                fh.write(dataall.encode('utf-8'))
                print('第' + str(i) + '个网页第' + str(i) + '次处理')
                i += 1
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


class control(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
    def run(self):
        while(True):
            print('程序执行中。')
            time.sleep(60)
            if (self.urlqueue.empty()):
                print("程序执行完毕！")
                exit()


key = '人工智能'
pro = ['61.135.217.7:80', '101.37.79.125:3128', '118.190.95.35:9001', '171.37.162.116:8123', '121.17.160.63:808',
       '118.190.95.35:9001', '202.112.237.102:3128', '113.200.56.13:8010', '113.128.148.31:8118',
       '110.40.13.5:80', '112.91.218.21	:9000']
proxy = '120.92.74.189:3128'
pagestart = 1
pageend = 2
t1 = geturl(key, pagestart, pageend, proxy, urlqueue)
t1.start()
t2 = getcontent(urlqueue, proxy)
t2.start()
t3 = control(urlqueue)
t3.start()