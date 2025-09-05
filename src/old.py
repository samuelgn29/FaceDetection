import cv2 as cv
import time
import numpy as np

# Open the default camera
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# used to record the time when we processed last frame
prev_frame_time = 0
# used to record the time at which we processed current frame
new_frame_time = 0

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    # if frame is read correctly ret is true
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Operations on the frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # font which we will be using to display FPS
    font = cv.FONT_HERSHEY_TRIPLEX
    # time when we finish processing for this frame
    new_frame_time = time.time()

    # calculating the fps
    # fps will be number of frame processed in given time frame since there
    # will be most of time error of 0.001 second we will be subtracting it
    # to get more accurate result
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    # converting the fps to integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame by
    # using putText function
    fps = str(fps)

    # putting the fps count on the frame
    cv.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA)
    # displaying the frame with fps
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# When opening done, release the capture
cap.release()
cv.destroyAllWindows()

