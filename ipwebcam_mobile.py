import cv2
import imutils
import numpy as np
import urllib.request

url = "http://192.168.0.101:8080/shot.jpg"
imgpath = urllib.request.urlopen(url)
imgnp = np.array(bytearray(imgpath.read()),dtype=np.uint8)
img = cv2.imdecode(imgnp,-1)
img = imutils.resize(img,width=450)
cv2.imshow("Mobile IPCamera",img)
if ord("q") == cv2.waitKey(1):
    exit(0)
