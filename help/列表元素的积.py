def func(lis, n):
    s = 1
    for i in lis:
        if i == lis[n]:
            continue
        s = s*i
    return s


ls = eval(input('请输入列表'))
lt = []
for x in range(len(ls)):
    lt.append(func(ls, x))
print(lt)