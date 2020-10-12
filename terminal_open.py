from pynput import keyboard
import os
import time

exit = False

def on_press(key):
	pass

def on_release(key):
	if key == keyboard.Key.esc:
		# Stop listener
		# global exit
		# exit = True
		os.system('xterm &')
		os.system("xdotool search --sync --class 'xterm' windowactivate key F11")
		print("opened")

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


while(not exit):
	time.sleep(1)