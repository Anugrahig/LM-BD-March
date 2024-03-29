
# web cam reading 
import cv2
import HandTrackingModule as htm
import numpy as np
import time



detector=htm.handDetector()

draw_color=(0,0,255)

# height ,width, channel
# black screen
img_canvas=np.zeros((720,1280,3),np.uint8)

p_time = 0



cap=cv2.VideoCapture(0)

while True:
  success,frame=cap.read()
  # resizing the frame
  
  frame=cv2.resize(frame,(1280,720))
  # 1 means horizontal flip
  # -1 mens vertical flip
  frame=cv2.flip(frame,1)
  # 1280/5-4*10
  
  # drawing Rectangle
  cv2.rectangle(frame,(10,10),(230,100),(0,0,255),cv2.FILLED)
  cv2.rectangle(frame,(240,10),(460,100),(0,255,0),cv2.FILLED)
  cv2.rectangle(frame,(470,10),(690,100),(255,0,0),cv2.FILLED)
  cv2.rectangle(frame,(700,10),(920,100),(0,255,255),cv2.FILLED)
  cv2.rectangle(frame,(930,10),(1270,100),(255,255,255),cv2.FILLED)
  cv2.putText(frame,"ERASER",(1040,70),fontScale=1,fontFace=cv2.FONT_HERSHEY_SIMPLEX,color=(0,0,0),thickness=3)
  
  
  # find hand landmarks
  
  frame=detector.findHands(frame,draw=True)
  lmlist=detector.findPosition(frame)
  # print(lmlist)
  
  if len(lmlist)!=0:
    x1,y1=lmlist[8][1:]
    x2,y2=lmlist[12][1:]
    # print(x1,y1)
    # when finger up 1
  # check which finger is up
    
    fingers = detector.fingersUp()
    # print(fingers)
    
    # selection mode - two finger is up
    
    if fingers[1] and fingers[2]:
      # xp,yp previous point
      xp,yp=0,0
      print("Selection Mode")
      if y1<100:
        if 10<x1<230:
          draw_color=(0,0,255)
          # print("red")
        elif 240<x1<460:
          
          draw_color=(0,255,0)
          # print("green")
          
        elif 470 < x1<690:
          draw_color=(255,0,0)
          # print("blue")
        elif 700<x1<920:
          draw_color=(0,255,255)
          
          # print("yellow")
        elif 930<x1<1270:
          draw_color=(0,0,0)
          
          # print("Eraser")
      
      # setting default color
      cv2.rectangle(frame,(x1,y1),(x2,y2),color=draw_color,thickness=cv2.FILLED)
      
      
    # drawing mode - index finger is up
    
    if fingers[1] and not fingers[2]:
      
      
      # print("Drawing Mode")
      cv2.putText(frame,"Drawing Mode",(1000,650),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,255,0),thickness=3)
      # radius =10
      cv2.circle(frame,(x1,y1),20,draw_color,thickness=-1)
      
      if xp==0 and yp==0:
        xp=x1
        yp=y1
        
      # eraser  one condition other color has one condition 
      
      # black color condition
      if draw_color==(0,0,0):
        cv2.line(frame,(xp,yp),(x1,y1),color=draw_color,thickness=50)
        cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=50)
      else:
        cv2.line(frame,(xp,yp),(x1,y1),color=draw_color,thickness=10)
        cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=10)

      xp,yp=x1,y1
      
      
      
      
  """
  # lmlist decect position of hands
  # 0 - 20 (first point) is landmarks
  # we need index finger and middle finger (from the hand land marks)
  # 8 & 12 we need points
  8 is the index finger
  12 is the middle finger
  """
  """
  
  x1,y1=[8],[1:]
  x2,y2=[12],[1:]
  """
  
  
  # Merging 2 canvas
  
  # convrt to gray scale
  # apply threshold
  # 

  # bgr to gray convertion 
  img_gray = cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY) # to gray
  
  # threshold inverse

  thresh,img_inv = cv2.threshold(img_gray,20,255,cv2.THRESH_BINARY_INV)
  # now color is black
  
  img_inv=cv2.cvtColor(img_inv,cv2.COLOR_GRAY2BGR)
  
  
  # AND OPERATIONS
  
  frame=cv2.bitwise_and(frame,img_inv)
  
  frame=cv2.bitwise_or(frame,img_canvas)


# canvas frame is .5 
# last value will be zero

# joing the frame
  cv2.addWeighted(frame,1,img_canvas,.5,0)   
  
  
  # calculating FPS
  
  c_time=time.time()
  # frame per second alculation
  fps=1/(c_time - p_time)
  
  p_time = c_time
  
  
  cv2.putText(frame,str(int(fps)),(50,200),cv2.FONT_HERSHEY_SIMPLEX,5,(0,0,0),4)
  
  
  cv2.imshow("Virtual Painter",frame)
  # one canvas for img drawing and another for color selection
  # cv2.imshow("Canvas",img_canvas)
  # cv2.imshow("Gray Image",img_inv)
  
  if cv2.waitKey(1)& 0xFF==27:
    break
cap.release()
cv2.destroyAllWindows()