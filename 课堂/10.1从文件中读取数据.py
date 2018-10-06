with open('pi_digit.txt') as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip()

pi_list=list(pi_string)

birthday=input('Enter your birthday,in the form mmddyy:')
birthday_list=list(birthday)

i=2
j=0
for num in pi_list[2:]:
    if num==birthday_list[0]:
        j=i
        f=True
        if i+len(birthday_list)>len(pi_list):
            print('NO!')
            break
        for n in birthday_list:
            if n!=pi_list[j]:
                f=False
            j+=1
        if f:
            print(i-1)
            break
    i+=1
if i>=len(pi_list):
    print('NO!')
