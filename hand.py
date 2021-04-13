import cv2
import mediapipe as mp
import math
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def add_picture(img, img2_path,x_split, y_split, height=50, width=50):
  img2 = cv2.imread(img2_path)
  img2 = cv2.resize(img2, (height, width))

  rows, cols, channels = img2.shape
  roi = img[x_split:(x_split + rows), y_split:(y_split + cols)]
  # print(roi)
  img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(img2gray, 200, 240, cv2.THRESH_BINARY)
  mask_inv = cv2.bitwise_not(mask)
  img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

  img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

  dst = cv2.add(img1_bg, img2_fg)
  img[x_split:(x_split + rows), y_split:(y_split + cols)] = dst

  return image


def write_calculate(image):
  image = add_picture(image, img2_path="./calculate/a.png",x_split=0,y_split=0)
  image = add_picture(image, img2_path="./calculate/b.png",x_split=0,y_split=55)
  image = add_picture(image, img2_path="./calculate/c.png",x_split=0,y_split=110)
  image = add_picture(image, img2_path="./calculate/d.png",x_split=0,y_split=165)
  image = add_picture(image, img2_path="./calculate/e.png",x_split=0,y_split=220)

  image = add_picture(image, img2_path="./calculate/f.png",x_split=55,y_split=0)
  image = add_picture(image, img2_path="./calculate/g.png",x_split=55,y_split=55)
  image = add_picture(image, img2_path="./calculate/h.png",x_split=55,y_split=110)
  image = add_picture(image, img2_path="./calculate/i.png",x_split=55,y_split=165)
  image = add_picture(image, img2_path="./calculate/j.png",x_split=55,y_split=220)

  image = add_picture(image, img2_path="./calculate/k.png",x_split=110,y_split=0)
  image = add_picture(image, img2_path="./calculate/l.png",x_split=110,y_split=55)
  image = add_picture(image, img2_path="./calculate/m.png",x_split=110,y_split=110)
  image = add_picture(image, img2_path="./calculate/n.png",x_split=110,y_split=165)
  image = add_picture(image, img2_path="./calculate/o.png",x_split=110,y_split=220)

  image = add_picture(image, img2_path="./calculate/p.png",x_split=165,y_split=0)
  image = add_picture(image, img2_path="./calculate/q.png",x_split=165,y_split=55)
  image = add_picture(image, img2_path="./calculate/r.png",x_split=165,y_split=110)
  image = add_picture(image, img2_path="./calculate/s.png",x_split=165,y_split=165)
  image = add_picture(image, img2_path="./calculate/t.png",x_split=165,y_split=220)

  image = add_picture(image, img2_path="./calculate/u.png",x_split=220,y_split=0)
  image = add_picture(image, img2_path="./calculate/v.png",x_split=220,y_split=55)
  image = add_picture(image, img2_path="./calculate/w.png",x_split=220,y_split=110)
  image = add_picture(image, img2_path="./calculate/x.png",x_split=220,y_split=165)
  image = add_picture(image, img2_path="./calculate/y.png",x_split=220,y_split=220)
  # image = add_picture(image, img2_path="./calculate/z.png",x_split=220,y_split=275)
  return image


# For webcam input:
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

while cap.isOpened():
  success, image = cap.read()
  # image = write_calculate(image)
  tex = ""
  word = ""

  if not success:
    print("Ignoring empty camera frame.")
    # If loading a video, use 'break' instead of 'continue'.
    continue
  cv2.namedWindow("camera", 0)
  cv2.resizeWindow("camera", 1920, 1080)
  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  # print(image.shape)

  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
  image.flags.writeable = True
  results = hands.process(image)

  # Draw the hand annotations on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  # cv2.imread("/calculate/1.png")
  if results.multi_hand_landmarks:

    for hand_landmarks in results.multi_hand_landmarks:

      # if (abs(hand_landmarks.landmark[4].x - hand_landmarks.landmark[17].x) and 
      #     abs(hand_landmarks.landmark[4].y - hand_landmarks.landmark[17].y)) <= 0.03 :
      #   print(hand_landmarks.landmark[4].x)

      # mp_drawing.draw_landmarks(
      #     image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

      finger_8_x = hand_landmarks.landmark[8].x
      finger_8_y = hand_landmarks.landmark[8].y
      # print("x : %f" % finger_8_x)
      # print("y--------------- : %f" % finger_8_y)

      if ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.03 and finger_8_y <= 0.12)) :
        cv2.rectangle(image, (20, 10), (80, 50), (55, 255, 155), thickness=-1)
        tex = 'A'
      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.03 and finger_8_y <= 0.12)) :
        cv2.rectangle(image, (95, 10), (155, 50), (55, 255, 155), thickness=-1)
        tex = 'B'
      elif ((finger_8_x >= 0.27 and finger_8_x <= 0.38) and (finger_8_y >= 0.03 and finger_8_y <= 0.12)) :
        cv2.rectangle(image, (170, 10), (230, 50), (55, 255, 155), thickness=-1)
        tex = 'C'
      elif ((finger_8_x >= 0.39 and finger_8_x <= 0.51) and (finger_8_y >= 0.03 and finger_8_y <= 0.12)) :
        cv2.rectangle(image, (240, 10), (300, 50), (55, 255, 155), thickness=-1)
        tex = 'D'

      elif ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.15 and finger_8_y <= 0.24)) :
        cv2.rectangle(image, (20, 70), (80, 110), (55, 255, 155), thickness=-1)
        tex = 'E'
      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.15 and finger_8_y <= 0.24)) :
        cv2.rectangle(image, (95, 70), (155, 110), (55, 255, 155), thickness=-1)
        tex = 'F'
      elif ((finger_8_x >= 0.27 and finger_8_x <= 0.38) and (finger_8_y >= 0.15 and finger_8_y <= 0.24)) :
        cv2.rectangle(image, (170, 70), (230, 110), (55, 255, 155), thickness=-1)
        tex = 'G'
      elif ((finger_8_x >= 0.39 and finger_8_x <= 0.51) and (finger_8_y >= 0.15 and finger_8_y <= 0.24)) :
        cv2.rectangle(image, (240, 70), (300, 110), (55, 255, 155), thickness=-1)
        tex = 'H'

      elif ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.27 and finger_8_y <= 0.36)) :
        cv2.rectangle(image, (20, 125), (80, 165), (55, 255, 155), thickness=-1)
        tex = 'I'
      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.27 and finger_8_y <= 0.36)) :
        cv2.rectangle(image, (95, 125), (155, 165), (55, 255, 155), thickness=-1)
        tex = 'J'
      elif ((finger_8_x >= 0.27 and finger_8_x <= 0.38) and (finger_8_y >= 0.27 and finger_8_y <= 0.36)) :
        cv2.rectangle(image, (170, 125), (230, 165), (55, 255, 155), thickness=-1)
        tex = 'K'
      elif ((finger_8_x >= 0.39 and finger_8_x <= 0.51) and (finger_8_y >= 0.27 and finger_8_y <= 0.36)) :
        cv2.rectangle(image, (240, 125), (300, 165), (55, 255, 155), thickness=-1)
        tex = 'L'

      elif ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.39 and finger_8_y <= 0.48)) :
        cv2.rectangle(image, (20, 180), (80, 220), (55, 255, 155), thickness=-1)
        tex = 'M'
      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.39 and finger_8_y <= 0.48)) :
        cv2.rectangle(image, (95, 180), (155, 220), (55, 255, 155), thickness=-1)
        tex = 'N'
      elif ((finger_8_x >= 0.27 and finger_8_x <= 0.38) and (finger_8_y >= 0.39 and finger_8_y <= 0.48)) :
        cv2.rectangle(image, (170, 180), (230, 220), (55, 255, 155), thickness=-1)
        tex = 'O'
      elif ((finger_8_x >= 0.39 and finger_8_x <= 0.51) and (finger_8_y >= 0.39 and finger_8_y <= 0.48)) :
        cv2.rectangle(image, (240, 180), (300, 220), (55, 255, 155), thickness=-1)
        tex = 'P'

      elif ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.51 and finger_8_y <= 0.60)) :
        cv2.rectangle(image, (20, 235), (80, 275), (55, 255, 155), thickness=-1)
        tex = 'Q'
      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.51 and finger_8_y <= 0.60)) :
        cv2.rectangle(image, (95, 235), (155, 275), (55, 255, 155), thickness=-1)
        tex = 'R'
      elif ((finger_8_x >= 0.27 and finger_8_x <= 0.38) and (finger_8_y >= 0.51 and finger_8_y <= 0.60)) :
        cv2.rectangle(image, (170, 235), (230, 275), (55, 255, 155), thickness=-1)
        tex = 'S'
      elif ((finger_8_x >= 0.39 and finger_8_x <= 0.51) and (finger_8_y >= 0.51 and finger_8_y <= 0.60)) :
        cv2.rectangle(image, (240, 235), (300, 275), (55, 255, 155), thickness=-1)
        tex = 'T'

      elif ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.63 and finger_8_y <= 0.72)) :
        cv2.rectangle(image, (20, 290), (80, 330), (55, 255, 155), thickness=-1)
        tex = 'U'
      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.63 and finger_8_y <= 0.72)) :
        cv2.rectangle(image, (95, 290), (155, 330), (55, 255, 155), thickness=-1)
        tex = 'V'
      elif ((finger_8_x >= 0.27 and finger_8_x <= 0.38) and (finger_8_y >= 0.63 and finger_8_y <= 0.72)) :
        cv2.rectangle(image, (170, 290), (230, 330), (55, 255, 155), thickness=-1)
        tex = 'W'
      elif ((finger_8_x >= 0.39 and finger_8_x <= 0.51) and (finger_8_y >= 0.63 and finger_8_y <= 0.72)) :
        cv2.rectangle(image, (240, 290), (300, 330), (55, 255, 155), thickness=-1)
        tex = 'X'

      elif ((finger_8_x >= 0.03 and finger_8_x <= 0.12) and (finger_8_y >= 0.75 and finger_8_y <= 0.84)) :
        cv2.rectangle(image, (20, 345), (80, 385), (55, 255, 155), thickness=-1)
        tex = 'Y'

      elif ((finger_8_x >= 0.15 and finger_8_x <= 0.25) and (finger_8_y >= 0.75 and finger_8_y <= 0.84)) :
        cv2.rectangle(image, (95, 345), (155, 385), (55, 255, 155), thickness=-1)
        tex = 'Z'

      image = cv2.putText(image, tex, (400, 300), cv2.FONT_HERSHEY_TRIPLEX, 7, (0, 0, 255), 7)

  img2 = cv2.imread("bg.jpg")
  img2 = cv2.resize(img2, (640, 480))
  image = cv2.addWeighted(image, 0.3, img2, 0.7,0)

  cv2.imshow('camera', image)
  if cv2.waitKey(5) & 0xFF == ord('q'):
    break
hands.close()
cap.release()