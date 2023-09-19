import cv2
# cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("open_cv/data/videoplayback.mp4")

left_eye_cascade=cv2.CascadeClassifier("open_cv/data/haarcascades/haarcascade_lefteye_2splits.xml")
smile_cascade=cv2.CascadeClassifier("open_cv/data/haarcascades/haarcascade_russian_plate_number.xml")

while True:
  success,frame=cap.read()
  gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  
  eyes=left_eye_cascade.detectMultiScale(gray_image)
  print(eyes)
  for (x,y,w,h) in eyes:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),4) 
  smiles=smile_cascade.detectMultiScale(gray_image)
  for (x,y,w,h) in smiles:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
  cv2.imshow("Video Detect",cv2.resize(frame,(720,720)))
  
  if cv2.waitKey(100) & 0xFF==27:
    break
cap.release()
cv2.destroyAllWindows()