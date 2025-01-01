import cv2
from config import LOG_FILE

class VideoModerator:
    def __init__(self):
        pass

    def moderate_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if self.detect_obscene_content(frame):
                self.log_violation(video_path)
                return "Inappropriate content detected in video."
        cap.release()
        return "Video is appropriate."

    def detect_obscene_content(self, frame):
        # Placeholder logic for detection
        return False

    def log_violation(self, video_path):
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"Violation detected in video: {video_path}\n")
