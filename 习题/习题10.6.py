print('Please enter two numbers, and I\'ll add them.')
print('enter \'q\' to quit.')
while True:
    first_number=input('Enter the first number:')
    if first_number=='q':
        break
    second_number=input('Enter the second number:')
    if second_number=='q':
        break
    try:
        first_number=int(first_number)
        second_number=int(second_number)
    except ValueError:
        print('Value error.')
    else:
        print(first_number+second_number)
