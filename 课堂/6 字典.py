alien_0={'color':'green','points':'5'}#创建字典
new_points=alien_0['points']
print('You just earned '+str(alien_0['points'])+' points!')
alien_0['x_position']=0#添加键-值对
alien_0['y_position']=25
print(alien_0)
alien_0['x_position']=1#对键-值对修改
print(alien_0)
alien_0['speed']='medium'
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("new position: "+str(alien_0['x_position']))
del alien_0['points']#删除键-值对
print(alien_0)
users={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in users.items():#遍历字典所有的键值对(方法items不可省略)
    print('\nKey:'+key)
    print('Value:'+value)
for name in users.keys():#遍历字典中所有的键
    print(name.title())
for name in users:#不使用key方法遍历所有的键
    print(name.title())
favourite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in sorted(favourite_language.keys()):#对键按首字母排序
    print(name.title()+',thank you for taking poll')
for v in favourite_language.values():#遍历字典中的所有值
    print(v.title())
for v in set(favourite_language.values()):#使用集合set剔除字典中重复的值
    print(v.title())
