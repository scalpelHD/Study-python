lis = eval(input('请输入列表：'))
'''
for i in range(len(lis)):
    if lis[i] == 0:
        j = i+1
        while j < len(lis):
            if lis[j] != 0:
                lis[i] = lis[j]
                lis[j] = 0
                break
            j = j+1
'''
n = lis.count(0)
while 0 in lis:
    lis.remove(0)
lis = lis + [0]*n
print(lis)
