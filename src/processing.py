import cv2 as cv

def to_gray(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return gray

def blur(frame):
    return cv.GaussianBlur(frame, (7, 7), 0)

def equalize_hist(frame):
    return cv.equalizeHist(frame)

def preprocess(frame):
    gray = to_gray(frame)
    blurred = blur(gray)
    return equalize_hist(blurred)

def detect_faces(frame, cascade):
    return cascade.detectMultiScale(frame, 1.1, 5, minSize=(40, 40))

