s = '''Rain is falling all around.It falls on field and tree.
It rains on the umbrella here.And on the ships at sea.'''
s = s.lower()
dir = {}
for c in s:
    dir[c] = s.count(c)
for k, v in dir.items():
    print((k, v))
