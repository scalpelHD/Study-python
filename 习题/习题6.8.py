#在列表中嵌套字典
peter={'speices':'dog','master':'Peterown','age':9}
jenny={'speices':'cat','master':'Jennyown','age':3}
tom={'speices':'mice','master':'Tomown','age':5}
pets=[peter,jenny,tom]
for pet in pets:
    print(pet)
#在在字典中嵌套列表
fav_places={
    'peter':['paris','newyork','beijing'],
    'lucy':['london','australia','brazil'],
    'ann':['shanghai','xian','berlin'],
    }
for name,places in fav_places.items():
    print('\n'+name.title()+"'s favourite places are:")
    for place in places:
        print(place.title())
#在字典中嵌套字典
cities={
    'newyork':{
        'country':'america',
        'famous':'economy',
        'language':'english',
        },
    'paris':{
        'country':'france',
        'famous':'fashion',
        'language':'french',
        },
    'london':{
        'country':'britain',
        'famous':'fog',
        'language':'english',
        },
    }
for city,infos in cities.items():
    print('\n'+city.title())
    print('\tNATION: '+infos['country'].title())
    print('\tFACT: '+infos['famous'])
    print('\tLANGUAGE: '+infos['language'].title())
