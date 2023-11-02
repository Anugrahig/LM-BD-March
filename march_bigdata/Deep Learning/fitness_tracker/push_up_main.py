import poseModule as pm
import cv2
import numpy as np


file1="fitness_tracker/push_up1.mp4"
file2="fitness_tracker/push_up1.mp4"

detector=pm.poseDetector()


cap = cv2.VideoCapture(file1)

count = 0
dir = 0

while True:
  success,img=cap.read()
  img=cv2.resize(img,(1280,720))
  
  img = detector.findPose(img,draw=False)
  lmlist = detector.findPosition(img,draw=False)
  
  if len(lmlist) !=0:
    angle = detector.findAngle(img,16,14,12)
    
    # print(angle)
    low = 230
    high = 290
    
    percentage = np.interp(angle,(low,high),(0,100))
    
    if percentage == 100:
      if dir == 0:
        count+=.5
        dir=1
    if percentage == 0:
      if dir ==1:
        count+=.5
        dir=0
    print(int(count))
   
  
  cv2.imshow("Video",img)
  
  if cv2.waitKey(10) & 0xFF==27:
    break
cap.release()
cv2.destroyAllWindows()

