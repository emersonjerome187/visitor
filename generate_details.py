import json
import random
import requests

# with open('names.json', 'r') as infile:
# 	names = json.load(infile)
quantity = 500
resp = requests.get('http://names.drycodes.com/'+str(quantity)+'?nameOptions=boy_names')
# index = 0
names = resp.json()
print(names)
# output = {}
# generate = ["Finley Scallop"]
# next_gen = []

accounts = []

# levels = 4

def scramble(string):
	l = list(string)
	random.shuffle(l)
	return ''.join(l)

def get_password():
	s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	s1 = "0123456789"
	s2 = "!@#$%^&*()?"
	p =  "".join(random.sample(s,5))
	p2 =  "".join(random.sample(s1,4))
	p3 =  "".join(random.sample(s2,5))
	return scramble(p+p2+p3)


for x in names:
	fn1 = x.split("_", 1)[0]
	ln1 = x.split("_", 1)[1]
	un1 = fn1 + ln1 + str(random.randint(0, 999))
	un1 = un1.lower()
	pw1 = get_password()
	accounts.append([un1, pw1, fn1, ln1])

try:
	with open('accounts.json', 'w') as outfile:
		json.dump(accounts, outfile)
except:
	pass



# for x in range(0,levels+1):
# 	for y in generate:
# 		if x == levels:
# 			output[y] = [0, ["", "", "", ""], ["", "", "", ""]]
# 		else:
# 			name1 = names[index]
# 			index += 1
# 			name2 = names[index]
# 			index += 1
# 			fn1 = name1.split(" ", 1)[0]
# 			ln1 = name1.split(" ", 1)[1]
# 			un1 = fn1 + ln1 + str(random.randint(0, 999))
# 			un1 = un1.lower()
# 			pw1 = get_password()
# 			fn2 = name2.split(" ", 1)[0]
# 			ln2 = name2.split(" ", 1)[1]
# 			un2 = fn2 + ln2 + str(random.randint(0, 999))
# 			un2 = un2.lower()
# 			pw2 = get_password()
# 			next_gen.append(name1)
# 			next_gen.append(name2)
# 			accounts.append([un1, pw1])
# 			accounts.append([un2, pw2])
# 			output[y] = [3, [fn1, ln1, un1, pw1], [fn2, ln2, un2, pw2]]
# 	generate = next_gen
# 	next_gen = []

# try:
# 	with open('acc_list.txt', 'w') as outfile:
# 		json.dump(output, outfile)
# except:
# 	pass
