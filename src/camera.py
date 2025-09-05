import cv2 as cv

class CameraHandler:

    def __init__(self, camera_id):
        self.camera_id = camera_id
        # Open the camrea
        self.cap = cv.VideoCapture(camera_id)
        if not self.cap.isOpened():
            print("Error while opening camera")

    def read_frame(self):
        # Capture each frame
        ret, frame = self.cap.read()

        # ret is true if the video is read correctly
        if not ret or frame is None:
            print("Can't receive frame")
            return None
        return frame

    def release(self):
        # Release the capture
        self.cap.release()
        cv.destroyAllWindows()