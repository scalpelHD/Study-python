responses={}
polling_active = True#设置标志，控制循环
while polling_active:
    name=input('\nWhat is your name?')
    response=input('Which mountain would you like to climb someday?')
    #将答卷储存在字典中
    responses[name]=response
    #看看是否还有人要参与调查
    repeat=input('Would you like to let another guy repond?')
    if repeat=='no':
        polling_active=False
#调查结束，显示结果
print('\n----Poll Result----')
for name,response in responses.items():
    print(name.title()+' would like to climb '+response+'.')
