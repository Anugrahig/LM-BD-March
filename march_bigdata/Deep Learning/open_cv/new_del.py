import cv2

video_capture=cv2.VideoCapture(0)

while True:
  success,frame=video_capture.read()
  if cv2.waitKey(10)& 0xFF == 27:
    break
  cv2.imshow("Video Playback",frame)
video_capture.release()
cv2.destroyAllWindows()