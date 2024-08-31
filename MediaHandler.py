import cv2  # OpenCV for video and image processing
import pyautogui

class MediaHandler:
    def __init__(self):
        # Predefined video resolutions and file formats
        self.STD_DIMENSIONS = {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160)
        }
        self.VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID')
        }

    def change_res(self, cap, width, height):
        """
        Sets the resolution for the video capture.
        """
        cap.set(3, width)
        cap.set(4, height)

    def get_dims(self, res='1080p'):
        """
        Returns the dimensions for the specified resolution.
        """
        return self.STD_DIMENSIONS.get(res, self.STD_DIMENSIONS['1080p'])

    def get_video_type(self, filename):
        """
        Returns the video file type based on the file extension.
        """
        filename, ext = filename.split('.')
        return self.VIDEO_TYPE.get(ext, self.VIDEO_TYPE['avi'])

    def record_video(self, filename="output.avi", res="1080p", fps=30):
        """
        Records a video from the webcam and saves it to a file.
        """
        cap = cv2.VideoCapture(0)
        dims = self.get_dims(res)
        video_type_cv2 = self.get_video_type(filename)

        self.change_res(cap, dims[0], dims[1])

        out = cv2.VideoWriter(filename, video_type_cv2, fps, dims)

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            cv2.imshow('Recording', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def capture_screenshot(self, filename="screenshot.png"):
        """
        Captures a screenshot and saves it to a file.
        """
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

# Example usage:
if __name__ == "__main__":
    media_handler = MediaHandler()

    # Example: Record a video
    media_handler.record_video(filename="test_video.avi", res="720p", fps=25)

    # Example: Capture a screenshot
    media_handler.capture_screenshot(filename="test_screenshot.png")
