from decaptcha.notarobot import NotARobot
import sys

janet = NotARobot()
janet.set_model("yolo.h5")
janet.run()