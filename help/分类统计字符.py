dir = {'大写字母': 0, '小写字母': 0, '数字': 0, '空格': 0, '其他字符': 0}
s = input()
for c in s:
    if c.isupper():
        dir['大写字母'] += 1
    elif c.islower():
        dir['小写字母'] += 1
    elif c.isdigit():
        dir['数字'] += 1
    elif c.isspace():
        dir['空格'] += 1
    else:
        dir['其他字符'] += 1
for k, v in dir.items():
    print(v, end=',')
