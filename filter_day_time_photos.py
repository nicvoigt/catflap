""" Stream und Kamera funktionieren nur, wenn die Fotos vom Stream selbst gewählt werden.
Die Kamera kann nämlich nur von einem einzigen "Programm" aufgerufen werden.

"""

from picamera import PiCamera
from gpiozero import MotionSensor, LED
from signal import pause
import time
import os
import random
import datetime
import glob

direction = "/home/catflap/foto_labeling/static/Unlabeled_photos/"
target_folder = "/home/catflap/foto_labeling/filtered"
os.chdir(direction)
photo_dir = [ file for file in glob.glob("*.jpg")if not  7 <int(file.split("__")[1].split("verz")[0].split("_")[0])<21]
print(photo_dir)


for index, photo in enumerate(photo_dir):
    new_link = os.path.join(target_folder, photo_dir[index])
    os.replace(os.path.join(direction,photo), new_link)



