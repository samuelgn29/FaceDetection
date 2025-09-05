import cv2 as cv

def draw_fps(frame, fps):
    cv.putText(frame, fps, (7, 70), cv.FONT_HERSHEY_TRIPLEX, 3, (100, 255, 0), 3, cv.LINE_AA)

def draw_text(frame, text, pos):
    return None

def draw_crosshair(frame):
    return None

def draw_faces(frame, faces):
    for (x, y, w, h) in faces:
         cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return frame
