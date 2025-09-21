# Screen Streaming with Flask, OpenCV, and MSS

This project captures your primary monitor’s screen in real time and streams it over HTTP as an **MJPEG video feed** using Flask.

## 🚀 Features

* Captures live screen using **MSS**
* Encodes frames with **OpenCV** (JPEG, 90% quality)
* Resizes output to **1080p** (can be changed to 720p for better performance)
* Streams via Flask at `http://localhost:8080/`
* Works cross-platform (Windows, macOS, Linux)

---

## 📦 Requirements

Make sure you have **Python 3.8+** installed. Install dependencies using:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
flask
opencv-python
mss
numpy
```

---

## ▶️ Running the App

1. **Clone or download** this repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:

   ```bash
   python app.py
   ```
4. Open your browser at:

   ```
   http://localhost:8080/
   ```

---

## ⚙️ Configuration

* **Monitor selection**:
  By default, it streams the **primary monitor** (`sct.monitors[1]`).
  If you want to stream another monitor, change the index:

  ```python
  monitor = sct.monitors[2]  # secondary monitor
  ```

* **Resolution**:
  Output is resized to `1920x1080`. To reduce bandwidth, change:

  ```python
  frame = cv2.resize(frame, (1280, 720))  # 720p
  ```

* **JPEG Quality**:
  Currently set to 90. You can lower for performance:

  ```python
  [int(cv2.IMWRITE_JPEG_QUALITY), 70]
  ```

---

## 🛠️ Notes

* This app streams as **MJPEG**, which is supported in most browsers.
* For smoother performance, reduce resolution and quality.
* If you plan to expose it over a network, ensure proper authentication and security.

---

## 📷 Example

After running, open `http://localhost:8080/` in your browser and you should see your live desktop being streamed.
