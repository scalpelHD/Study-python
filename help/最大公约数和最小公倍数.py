def gys(a, b):
    if a < b:
        c = a
        a = b
        b = c
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def gbs(a, b):
    return int(a*b/gys(a, b))


x = int(input())
y = int(input())
print(gys(x, y))
print(gbs(x, y))
