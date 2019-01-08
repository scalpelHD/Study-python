def isdiff(n):
    n = str(n)
    flag = 0
    if len(n) != len(set(n)):
        flag = 1
    '''
    for c in n:
        if n.count(c) > 1:
            flag = 1
            break
    '''
    return flag


x = eval(input())
if isdiff(x):
    print('有重复数字')
else:
    print('无重复数字')
