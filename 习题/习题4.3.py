numbers=list(range(1,1000001))#创建列表
print(min(numbers),max(numbers),sum(numbers))#输出列表中的最大值和最小值以及和
nums=list(range(1,21,2))#输出1到20之间的奇数
for num in nums:
    print(num)
num2s=list(range(3,31,3))#输出3到30之间的倍数
for num2 in num2s:
    print(num2)
lifangs=[]#使用一般方法生成1到10的立方列表
for i in range(1,11):
    lifangs.append(i**3)
    print(i**3)
print(lifangs)
lifang2s=[i**3 for i in range(1,11)]#使用列表解析生成1到10的立方列表
print(lifang2s)
