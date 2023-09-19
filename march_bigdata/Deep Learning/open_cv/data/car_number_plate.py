import cv2

cap=cv2.VideoCapture("open_cv/data/car_number.mp4")
# cap=cv2.VideoCapture(0)

number_plate_cascade=cv2.CascadeClassifier("open_cv/data/haarcascades/haarcascade_russian_plate_number.xml")
# number_plate_cascade=cv2.CascadeClassifier("open_cv/data/haarcascades/haarcascade_license_plate_rus_16stages.xml")
img=[]
while True:
  success,frame=cap.read()
  gray_imgae=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  number_plates=number_plate_cascade.detectMultiScale(gray_imgae)
  # cv2.imshow("Number Plate Detect1",cv2.resize(frame,(720,720)))
  
  for i,(x,y,w,h) in enumerate(number_plates):
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    # frame=frame[y:y+h,x:x+w]
    number = frame[y:y + h, x:x + w]
    print(len(number))
    # img=frame[y:y+h,x:x+w]
    # if len(number) !=0:
    cv2.imwrite(f"open_cv/data/car_image/{i}.jpg", cv2.resize(number,(720,720)))
  # cv2.imwrite("../data/numper_plate.jpg",frame)
  cv2.imshow("Number Plate Detect",cv2.resize(frame,(720,720)))
  if cv2.waitKey(100) & 0xFF==27:
    break
cap.release()
cv2.destroyAllWindows()