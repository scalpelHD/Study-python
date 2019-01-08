def func(a):
    a = str(a)
    s = 0
    for c in a:
        s += int(c)
    return s


for x in range(100, 1001):
    flag = True
    for y in range(3, 8):
        if func(y*x) != func(3*x):
            flag = False
            break
    if flag:
        print(x)
        