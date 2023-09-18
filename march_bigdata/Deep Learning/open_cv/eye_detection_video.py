import cv2

# cap=cv2.VideoCapture("open_cv/data/videoplayback.mp4")
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("open_cv/data/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("open_cv/data/haarcascade_eye.xml")
while True:
  success,frame=cap.read()
  gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces=face_cascade.detectMultiScale(gray_img)
  eyes=eye_cascade.detectMultiScale(gray_img)
  # print(faces)
  for (x,y,w,h) in faces:
    face_img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
  for (x,y,w,h) in eyes:
    eye_img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
  cv2.imshow("Face detect Image",frame)
  if cv2.waitKey(100) & 0xFF==27:
    break
cap.release()
cv2.destroyAllWindows()