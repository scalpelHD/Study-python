def check(a):
    m = len(str(a))
    a0 = a
    s = 0
    a = str(a)
    for c in a:
        s += int(c)**m
    '''
    while a != 0:
        b = a % 10
        s += b**n
        a = a // 10
    '''
    if s == a0:
        return True
    else:
        return False


n = int(input('请输入n的值：'))
for x in range(10**(n-1), 10**n):
    if check(x):
        print(x)
