import cv2
import os
import datetime

akt_zeit = datetime.datetime.now()

image_folder = '/home/catflap/foto_labeling/static/Unlabeled_photos'
video_name = str(akt_zeit) + 'video.avi'

images = [os.path.join(image_folder,img) for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort(key=os.path.getctime)
frame = cv2.imread(images[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 10, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
cv2.flip(video, 0)
video.release()