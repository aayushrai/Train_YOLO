import os
import cv2
c = 0
for name in os.listdir('C:\\Users\\deadl\\Downloads\\YOLOv3-object-detection-tutorial-master\\YOLOv3-custom-training\\downloads\\speed limit sign'):
    ext = list(name.split('.'))[-1]
    if ext in ['jpg','png','jpeg']:
        image = cv2.imread('C:\\Users\\deadl\\Downloads\\YOLOv3-object-detection-tutorial-master\\YOLOv3-custom-training\\downloads\\speed limit sign\\' + name)
        c = c+1
        image = cv2.resize(image,(416,416))
        cv2.imwrite('C:\\Users\\deadl\\Downloads\\YOLOv3-object-detection-tutorial-master\\YOLOv3-custom-training\\downloads\\speed limit sign resize\\'+ str(c) +'.jpg',image)