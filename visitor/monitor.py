import json


log = input("view log y/n:")
if(log == "y"):
	with open('log.txt', 'r') as outfile:
		log = json.load(outfile)
		for x in log["log"]:
			print(x)
else:
	vc = input("view collector y/n:")
	if vc == 'y':
		collector = input("collector name:")
		with open('balances.txt', 'r') as outfile:
			log = json.load(outfile)
			claims = log[collector]
			for x in claims:
				print(x[0] + ' : ' + str(x[1]))