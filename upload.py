import os
import json
import os.path
from os import path

bot_name = os.getenv('BOT_NAME')

with open('/home/' + bot_name + '.txt', 'r') as infile:
		config = json.load(infile)

os.system('rm -dr upload')
os.system('mkdir upload')
# os.system('tar -cJf upload/chromium.tar.xz chromium')
os.system('tar -cJf - chromium | split --bytes=1m --suffix-length=4 --numeric-suffix - upload/chromium.tar.xz.')
os.system('megarm --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' /Root/upload')
os.system('megamkdir --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' /Root/upload')

# os.system('megarm --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' /Root/.mozilla/firefox/v2rtf8oi.default-release/cookies.sqlite-wal')
# os.system('megarm --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' /Root/.mozilla/firefox/v2rtf8oi.default-release/cookies.sqlite.bak')
for x in range(0,5):
	os.system('megacopy --reload --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' --remote /Root/upload --local /home/upload/')

os.system('megarm --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' /Root/timeouts.txt')
for x in range(0,3):
	os.system('megaput --reload --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' --path /Root/ visitor/timeouts.txt')

# def upload_dir_with_check(max_passes, remote_path):
# 	for x in range(1,max_passes):

# 		uploaded = 0

		

# 		if uploaded == 0:
# 			os.system('megaput --username ' + config['mega_username'] + ' --password ' + config['mega_password'] + ' --path /Root/ /home/chromium.tar.xz')
# 		else:
# 			break