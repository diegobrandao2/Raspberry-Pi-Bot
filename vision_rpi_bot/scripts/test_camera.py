import numpy as np
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    #capture frame by frame
    ret, frame = cap.read()
    #if frame is read correctly ret is true
    if not ret:
        print("can't receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(gray)
    #cv2.imshow('frame' , gray)
    #if cv2.waitKey(1) == ord('q'):
        #break
#when all done, release capture
cap.release()
cv2.destroyAllWindows()