alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','pinots':15}
aliens=[alien_0,alien_1,alien_2]#在列表中嵌套字典
for alien in aliens:
    print(alien)
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
print(str(len(aliens)))
for alien in aliens[:3]:#修改列表中的字典
    if alien['color']=='green' :
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
for alien in aliens[:5]:
    print(alien)
for alien in aliens[:5]:
    if alien['color']=='yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'
    elif alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
for alien in aliens[:5]:
    print(alien)
#在字典中嵌套列表
pizza={
    'crust':'thick',
    'topping':['mushroom','extra cheese'],
    }
print('You ordered a '+pizza['crust']+'-crust pizza'+
      ' with the following topping:')
for topping in pizza['topping']:
    print('\t'+topping)
#在字典中嵌套字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,user_info in users.items():
    print('\nUsername: '+username.title())
    full_name=user_info['first']+' '+user_info['last']
    location=user_info['location']

    print('\tFull name: '+full_name.title())
    print('\tLocation: '+location.title())
