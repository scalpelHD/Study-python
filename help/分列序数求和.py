n = eval(input())
s = 0
a, b = 1, 2
for x in range(n):
    s += b / a
    b = a + b
    a = b - a
print(s)
