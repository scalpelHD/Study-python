import re


pattern = '\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*'

string = "<a href = 'http://www.baidu.com'>百度首页</a><br><a href = '1151587242@qq.com'>电子邮件地址</a>"
print(re.search(pattern, string))
