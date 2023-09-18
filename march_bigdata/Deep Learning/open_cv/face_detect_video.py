import cv2


# video_capture=cv2.VideoCapture("open_cv/data/mh.mp4")

video_capture=cv2.VideoCapture("open_cv/data/videoplayback.mp4")
# video_capture=cv2.VideoCapture(0)


face_cascade=cv2.CascadeClassifier("open_cv/data/haarcascade_frontalface_default.xml")

while True:
  success,frame=video_capture.read()

  gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces=face_cascade.detectMultiScale(gray_img)
  for (x,y,w,h) in faces:
    rect_image=cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=4)
  cv2.imshow("V,ideo capture",frame)
  
  if cv2.waitKey(100)& 0xFF==27:
    break
video_capture.release()
cv2.destroyAllWindows()
  