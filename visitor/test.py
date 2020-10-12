import importlib.machinery
import Xlib.display
import os
import pyautogui

name = input("name: ")

module = importlib.machinery.SourceFileLoader(name, name+'/'+name+'.py').load_module()

pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

func = getattr(module, name)
print(func())