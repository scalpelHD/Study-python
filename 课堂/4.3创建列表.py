squares=[]
for i in range(1,11):
    print(i**2)
    squares.append(i**2)
print(squares)
print(min(squares),max(squares),sum(squares))
squares2=[i**2 for i in range(1,11)]
print(squares2)
    
