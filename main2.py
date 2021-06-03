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
direction = "/home/catflap/foto_labeling/static/Unlabeled_photos/"

pir = MotionSensor(23)
camera = PiCamera()
camera.hflip=True
camera.vflip=True

time.sleep(60)

while True:
    zeit1 = time.time()
    if not 7 < datetime.datetime.now().hour < 20:

        if pir.motion_detected:
            print("Bewegung erkannt")
            verzoegerung = 0.5
            time.sleep(verzoegerung)



            dir_time = time.strftime("%Y_%m_%d__%H_%M_%S")
            prefix =  dir_time + "_verz_" + str(verzoegerung) + "_"
            # for i in range(5):
                #camera.capture(os.path.join(new_dir, "image%s.jpg" % i ),use_video_port=True)
            camera.start_preview()
            camera.capture_sequence([os.path.join(direction, prefix + 'image%02d.jpg' % i)
                for i in range(5)], use_video_port= True)
            time.sleep(1)
            camera.stop_preview()
            zeit2 = time.time()

            print(zeit2-zeit1)
        
        
 






