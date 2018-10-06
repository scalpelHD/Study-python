import json
print('hello,world')
filename='first.json'
temps=[]
while True:
	temp=input('What is your name?')
	temps.append(temp)
	if temp=='q':
		break
with open(filename,'w') as f_obj:
	json.dump(temps,f_obj)
	
