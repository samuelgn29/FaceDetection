import time
import cv2 as cv

from src.camera import CameraHandler
from src import config
from src import processing
from src import overlay
from src import utils

# Open the camera with CAMERA_ID from config
camera = CameraHandler(config.CAMERA_ID)

# used to record the time when we processed last frame
prev_time = time.time()
# used to record the time at which we processed current frame
current_time = 0
cascade = "../models/haarcascade_frontalface_default.xml"
face_classifier = cv.CascadeClassifier(cascade)

while True:
    frame = camera.read_frame()

    current_time = time.time()
    fps = utils.calculate_fps(current_time, prev_time)
    prev_time = current_time

    preprocessed = processing.preprocess(frame)

    overlay.draw_fps(preprocessed, fps)
    overlay.draw_fps(frame, fps)

    detected_faces = processing.detect_faces(preprocessed, face_classifier)
    faces = overlay.draw_faces(frame, detected_faces)
    cv.imshow('faces', faces)
    cv.imshow('preprocessed', preprocessed)


    key = cv.waitKey(1)
    # Take a Screenshot when SCREENSHOT_KEY gets pressed
    if key == ord(config.SCREENSHOT_KEY):
        utils.save_screenshot(preprocessed)

    # Leave loop when QUIT_KEY gets pressed
    if key == ord(config.QUIT_KEY):
        break

camera.release()


