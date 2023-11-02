"""
# finpose : find a human body,if yes a draw 
# findposition : return a list (lm list ) x,y & landmark,-> draw + location , (cordinate)
# findAngle : 3 position to get an angle
"""

import poseModule as pm
import cv2
import numpy as np

file="/home/anugrah/Python Dev/LM-BD-March/march_bigdata/Deep Learning/fitness_tracker/squat.mp4"
detector=pm.poseDetector()

cap=cv2.VideoCapture(file)

while True:
  success,img=cap.read()
  img=cv2.resize(img,(1280,720))
  
  img=detector.findPose(img,draw=False)
  lmlist=detector.findPosition(img,draw=False)
  # print(lmlist)
  
  # find angles
  
  if len(lmlist) !=0:
    # img,p1,p2,p3
    angle= detector.findAngle(img,24,26,28)
    
    # we need to find low and highest angle
    
    low = 35
    high =170
    
    # 35 -> 0%
    #  170 -> 100%
    # any values from angle it convert to in b/w 0 & 100
    # we are calculate %
    percentage=np.interp(angle,(low,high),(0,100))
    
    print(angle,"-------->",percentage)
    
    # print(angle)
  
  cv2.imshow("Video",img)
  if cv2.waitKey(100) & 0xFF == 27:
    break
cap.release()
cv2.destroyAllWindows()
