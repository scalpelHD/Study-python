with open('D:\python文件\guest.txt','w') as file_object:
    while True:
        name=input('Please enter your name(enter \'q\' to quit):')
        if name=='q':
            break
        print('Hello!'+name+'.')
        file_object.write(name+' have logined!\n')
