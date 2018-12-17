import urllib.request
import re


# 爬取糗事百科上的段子
def getcontent(url, page):
    """模拟成浏览器"""
    headers = ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/71.0.3554.0 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    # 构建提取对应用户的正则表达式
    userpat = '<h2>(.*?)</h2>'
    # 构建提取段子的正则表达式
    contentpat = '<span>(.*?)</span>'
    # 寻找所有用户
    userlist = re.compile(userpat, re.S).findall(data)
    # 寻找所有的内容
    contentlist = re.compile(contentpat, re.S).findall(data)
    # 通过循环遍历段子内容并将段子内容分别赋给对应的变量
    x = 1
    for content in contentlist:
        content = content.replace("\n", "")
        content = content.replace("<br/>", "\n")
        # 用字符串作为变量名，先将对应字符串赋给一个变量
        name = "content"+str(x)
        # 通过exec()函数实现用字符串作为变量名并赋值
        exec(name+'=content')
        x += 1
    y = 1
    # 通过for循环遍历用户，并输出该用户对应的内容
    for user in userlist:
        name = "content"+str(y)
        user = user.replace("\n", '')
        print("第"+str(page)+"页第"+str(y)+"个用户是："+user)
        print("内容是：")
        exec("print("+name+")")
        print("\n")
        y += 1


for i in range(1, 3):
    if i == 1:
        url = 'https://www.qiushibaike.com/text/'
    else:
        url = "https://www.qiushibaike.com/text/page/"+str(i)+"/"
    getcontent(url, i)

