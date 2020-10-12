import os
import os.path
from os import path
import json
from mega import Mega

pastebin = os.getenv('PASTEBIN');

os.system('echo $(curl ' + pastebin + ') >> init.txt')
with open('init.txt', 'r') as infile:
	init = json.load(infile)

# for x in range(0,3):
# 	os.system('megadl ' + init["acc_list"])
# 	if path.exists('acc_list.txt'):
# 		print("downloaded acc_list")
# 		break

mega = Mega()
m = mega.login()
for x in range(0,5):
	m.download_url(init['source'])
	if path.exists('visitor.tar.xz'):
		print("Downloaded source")
		break
os.system('tar -xf ' + 'visitor.tar.xz')

# for x in range(0,3):
# 	os.system('megadl ' + init["proxy_config"])
# 	if path.exists('proxychains.conf'):
# 		print("downloaded proxy config")
# 		os.system("touch up.txt")
# 		break

os.system('mkdir upload')
for x in range(0,5):
	m.download_url(init['browser_config'])
	if path.exists('chromium.tar.xz'):
		print("Downloaded browser config")
		break
os.system('tar -xf ' + 'chromium.tar.xz')