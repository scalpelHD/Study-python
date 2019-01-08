x = int(input('请输入年份：'))
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print('366')
else:
    print('365')
