rivers={
    'nile':'egypt',
    'yangtze':'china',
    'amezon':'brizal',
    'messibi':'america',
    }
for k,v in rivers.items():#使用items方法遍历所有的键对值
    print('The '+k.title()+' runs through '+v.title())
for k in rivers.keys():#使用keys方法遍历所有的键
    print(k.title())
for v in sorted(rivers.values()):#使用sorted临时排序，使用values方法遍历所有的值
    print(v.title())
fav_lan={
    'jen':'c',
    'edward':'python',
    'ann':'java',
    'dana':'python',
    'luby':'ruby',
    'jerry':'php',
    }
yglist=['dana','jessy','jerry','jen','tom','tony','jhon']
for name in yglist:#遍历列表
    if name in fav_lan.keys():
        print('Mr.'+name.title()+',thank you for taking poll\n')
    else:
        print('Mr.'+name.title()+',please take poll as soon as possible!\n')
