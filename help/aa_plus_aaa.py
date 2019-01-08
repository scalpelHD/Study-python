def func(c, b):
    s = 0
    for y in range(b):
        s += c*(10**y)
    return s


a, n = eval(input('请输入a和n的值（用逗号分开）：'))
sum = 0
for x in range(0, n+1):
    sum += func(a, x)
print(sum)
