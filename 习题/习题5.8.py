names=['admin','peter','crystal','renoe','ann']
if names:#检查列表是否为空
    for name in names:#遍历列表
        if name=='admin':
            print('Hello Admin,would you like to see a status report?\n')
        else:
            print('Hello '+name.title()+',thank you for logging in again.\n')
else:
    print('列表为空！We need to find some users!')
del names[:]#删除列表
if names:#检查列表是否为空
    for name in names:#遍历列表
        if name=='admin':
            print('Hello Admin,would you like to see a status report?\n')
        else:
            print('Hello '+name.title()+',thank you for logging in again.\n')
else:
    print('列表为空！We need to find some users!')
current_users=['newton','einstan','ufo','uso','nick']
new_users=['dick','Einstan','UFO','peter','yangtze']
for new_user in new_users:#检查新用户名是不是已经存在
    if new_user.lower() in current_users:
        print(new_user+' has existed !,Please input another nickname!')
numbers=list(range(1,11))#创建1到10的数字列表
for number in numbers:#分类输出
    if number==1:
        print('FIRST')
    elif number==2:
        print('SECOND')
    elif number==3:
        print('THIRD')
    else:
        print(str(number)+'TH')

