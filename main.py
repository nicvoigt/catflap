from picamera import PiCamera
from gpiozero import MotionSensor, LED
from signal import pause
import time
import os
direction = "/home/catflap/pictures/"

pir = MotionSensor(23)
camera = PiCamera()

while True:
    zeit1 = time.time()
    if pir.motion_detected:
        
        print("Bewegung erkannt")
        time.sleep(.5)
        dir_time = time.strftime("%Y_%m_%d__%H_%M_%S")
        new_dir = os.path.join(direction, dir_time) 
        os.mkdir(new_dir)
        # for i in range(5):
            #camera.capture(os.path.join(new_dir, "image%s.jpg" % i ),use_video_port=True)
        camera.start_preview()
        camera.capture_sequence([os.path.join(new_dir,'image%02d.jpg' % i)
            for i in range(5)], use_video_port= True)
        time.sleep(.1)
        camera.stop_preview()
        zeit2 = time.time()
        
        print(zeit2-zeit1)
        
        break
 





