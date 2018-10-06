cars=['AUDI','Toyota','bmw','honda','beijing','jeep','beiJING']#if语句
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
    if car.lower()=='audi' or car.upper()=='TOYOTA':#或
        print(car.title())
    if car.lower()=='beijing' and car!='beiJING':#与
        print(car)
if 'honda' in cars:#检查特定值是否包含在列表中
    print('The honda is existed in the list!')
if 'auto' not in cars:#检查特定值是否不包含在列表中
    print('The auto is not existed in the list!')
#if-else语句
ages=[19,18,17,20]
names=['peter','tony','tom','jhon']
i=0
for age in ages:
    if age>=18:
        print('MR.'+names[i].title()+',you are old enough to vote!')
        print('Have you registered to vote yet?\n')
    else:
        print('MR.'+names[i].title()+',sorry,you are too young to vote.')
        print('Please register to vote as soon as you turn 18\n')
    i+=1
#if-elif-else语句
for age in ages:
    if age<=18:
        print('Your admission cost is $0.')
    elif age<20:
        print('Your admission cost is $5.')
    else:
        print('Your admission cost is $10.')
