def judge(password):
    degree = 0
    for c in password:
        if c.isdigit():
            degree += 1
            break
    for c in password:
        if c.isupper():
            degree += 1
            break
    for c in password:
        if c.islower():
            degree += 1
            break
    if len(password) >= 8:
        degree += 1
    return degree


passwords = input()
print('{}的密码强度为{}级。'.format(passwords, judge(passwords)))
