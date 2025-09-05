import cv2 as cv

def calculate_fps(current_time, prev_time):
    fps = 1 / (current_time - prev_time)
    fps = int(fps)
    fps = str(fps)
    return fps

def save_screenshot(gray_frame):
    cv.imwrite('../data/Screenshot.jpg', gray_frame)
