import cv2
# to read vide cam
video_capture=cv2.VideoCapture(0)
# to read a camera
# video_capture=cv2.VideoCapture("/home/anugrah/Python Dev/LM-BD-March/march_bigdata/Deep Learning/open_cv/data/mh.mp4")


while True:
  sucess,frame=video_capture.read()
  
  print(sucess)
  
  cv2.imshow("Video Capture",frame)
  
  if cv2.waitKey(1) & 0xFF==27:
    break
video_capture.release()
cv2.destroyAllWindows()