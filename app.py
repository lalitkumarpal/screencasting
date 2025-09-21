import cv2
import numpy as np
import mss
from flask import Flask, Response

app = Flask(__name__)

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # primary monitor
        while True:
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            # Resize to 1080p (change to 720p for smoother performance)
            frame = cv2.resize(frame, (1920, 1080))

            # Encode with high quality JPEG
            ret, buffer = cv2.imencode(
                '.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            )
            if not ret:
                continue
            frame_bytes = buffer.tobytes()

            # Yield as MJPEG stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def video_feed():
    return Response(capture_screen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)
