flag=True#披萨配料
while flag:
    adding=input('Please input the addings you want:')
    if adding=='quit':
        flag=False
    if adding!='quit':
        print('OK,we\'ll add the '+adding)
#film ticket
while 1:
    age=int(input('How old are you?Please input your age!\n'))
    if age<3:
        print('You are free!\n')
    elif age<12:
        print('Your ticket price is $10 per person!\n')
    else:
        print('Your ticket price is $15 per person!\n')
    question=input('Would you like go on?\n')
    if question=='no':
        break
