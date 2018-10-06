names=['giant', 'dog', 'lion', 'tiger', 'panda', 'puma', 'fish']
print('MR.'+names[0].title()+',welcome to my feast!')
i=0
while i<7:
    print('MR.'+names[i].title()+',welcome to my feast!')
    i+=1
print('What a pity!'+'MR.'+names[2].title()+" can't attend my feast!")
names[2]='wolf'
i=0
while i<7:
    print('MR.'+names[i].title()+',welcome to my feast!')
    i+=1
print('I find a bigger table just now!')
names.insert(0,'pig')
names.insert(4,'mice')
names.append('duck')
i=0
while i<10:
    print('MR.'+names[i].title()+',welcome to my feast!')
    i+=1
print(len(names))
while i>2:
    print('Sorry,MR.'+names.pop().title()+",you can't arrive my feast!")
    i-=1
print('MR.'+names[0].title()+',you also can go to my feast!')
print('MR.'+names[1].title()+',you also can go to my feast!')
del names[:]
print(len(names))
