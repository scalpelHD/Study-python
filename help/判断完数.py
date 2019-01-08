def func(a):
    s = 0
    for x in range(1, a):
        if a % x == 0:
            s += x
    if s == a:
        return True
    else:
        return False


for y in range(1, 1001):
    if func(y):
        print(y)