from ultralytics import YOLO
import cv2
import time

img = ["./WhatsApp Image 2023-05-25 at 13.49.30.jpeg"]
img2 = ["./crackedPipe.jpg"]
YOLO('./best.pt').predict(img, save = True, show = True)
time.sleep(10)
YOLO('./best.pt').predict(img2, save = True, show = True)
time.sleep(100)