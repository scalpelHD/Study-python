#8.6
def city_country(city,country):
    return city+','+country

while True:
    print('Please input a city and a coutry it belonged(enter \'q\' to quit):')

    city=input('city:')
    if city=='q':
        break
    
    country=input('country:')
    if country=='q':
        break
    
    citry=city_country(city,country)

    print(citry)

#8.7
def make_album(singer,name,number=''):
    """歌手和专辑信息"""
    info={'singer':singer,'name':name}
    if number:
        info['number']=number
    return info

while True:
    singer=input('Please input singer\'name(enter \'q\' to quit):')
    if singer=='q':
        break

    name=input('Please input album\'name:')
    if name=='q':
        break
    question=input('Would you like add the number of the album?')
    if question=='yes':
        num=int(input('Please input:'))
        print(make_album(singer,name,num))
    else:
        print(make_album(singer,name))
