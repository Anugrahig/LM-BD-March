import cv2
# to read vide cam
# video_capture = cv2.VideoCapture(0)
# to read a camera
video_capture=cv2.VideoCapture("open_cv/data/videoplayback.mp4")


while True:
  sucess,frame=video_capture.read()
  # rect_frame=cv2.rectangle(frame,pt1=(40,40),pt2=(300,315),color=(255,0,0),thickness=cv2.FILLED)
  # cir_frame=cv2.circle(rect_frame,center=(177,181),radius=100,color=(0,0,255),thickness=5)
  gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  (thresh,bw_img)=cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
  
          
  print(sucess)
  
  cv2.imshow("Video Capture",bw_img)
  
  if cv2.waitKey(100) & 0xFF==27:
    break
video_capture.release()
cv2.destroyAllWindows()