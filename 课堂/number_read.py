import json
filename='numbers.json'
with open(filename) as f_obj:
	number=json.load(f_obj)
	
print(number)
