#修改字符串（Python中字符串是不可变类型）
#切片修改
string='i Love vchina'
string=string[:2]+'l'+string[3:]
print(string)
string=string[:7]+string[-5:]
print(string)
string=string[:7]+'C'+string[8:]
print(string)

#将字符串转换成列表后修改值，然后用join组成新字符串
s='chinna'
s1=list(s)
s1.remove('n')
s1[0]='C'
s=''
s=s.join(s1)
print(s)

#使用字符串的replace函数
s='china'
s=s.replace('c','C')
print(s)

#重新赋值或者变量赋值
s='Hello world'
s1='2018'
s=s+','+s1
print(s)#变量赋值
s='Hello world'
s='Hello world,2018'
print(s)#重新赋值
