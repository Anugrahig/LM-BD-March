import cv2
import mediapipe as mp


video_capture=cv2.VideoCapture(0)

# access mediapipe functions
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.3)
mp_drawings=mp.solutions.drawing_utils
# read frames from webcam
while True:
  success,frame=video_capture.read()
  frame=cv2.resize(frame,(1000,1000))
  
  
  # print(sucess)
  
  
  

# detect hands

  results=hands.process(frame)

  if results.multi_hand_landmarks:
    # we need to group left and right groups
    for hand_no,hand_landmarks in enumerate(results.multi_hand_landmarks):
      # drawing
      mp_drawings.draw_landmarks(
        image=frame,
        landmark_list=hand_landmarks,
        connections = mp_hands.HAND_CONNECTIONS
      )
      # connecting line is mp_hands.HAND_CONNECTIONS
      # plt.imshow(rgb_img)


# draw lines

# show in window

  cv2.imshow("Video Capture",frame)
  
  if cv2.waitKey(1) & 0xFF==27:
    break
video_capture.release()
cv2.destroyAllWindows()