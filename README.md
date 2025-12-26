# AI  Privacy Guard 🛡️

A real-time AI-powered system designed to ensure privacy in video streams by automatically detecting and blurring human subjects.

---

##  Overview
The **AI  Privacy Guard** is a specialized computer vision application. It identifies human presence in a live video feed and applies an instantaneous Gaussian blur to ensure anonymity while keeping the rest of the environment visible.

##  Key Features
* **Real-time Detection:** Utilizes YOLO11 Nano for high-speed, low-latency inference.
* **Intelligent Blurring:** Specifically targets the 'person' class, leaving other objects (laptops, books, etc.) unblurred.
* **Custom ROI Processing:** Implements a specialized Region of Interest (ROI) extraction and replacement pipeline.
* **Dynamic UI:** Includes a "Privacy Filter" status label that moves with the subject.

##  Technical Stack
* **Programming Language:** Python 3.13
* **Deep Learning:** YOLO11 (Ultralytics)
* **Image Processing:** OpenCV (cv2)

##  Project Structure
* `personal_guard.py` - Core logic and image processing pipeline.
* `yolo11n.pt` - Pre-trained YOLO11 weights.
* `requirements.txt` - Required Python dependencies.

##  Credits & References
This project is built using the **Ultralytics YOLO11** framework as the underlying detection engine. 
* **Reference:** [Ultralytics GitHub](https://github.com/ultralytics/ultralytics)
* **My Contribution:** Beyond the base detection, I designed and implemented the **Selective Anonymization Logic**, handling ROI extraction, Gaussian smoothing, and real-time frame re-injection.

##  Installation & Usage
1.  **Install Requirements:**
    ```bash
    pip install ultralytics opencv-python
    ```
2.  **Run the Application:**
    ```bash
    python personal_guard.py
    ```
3.  **Exit:** Press **'q'** on your keyboard to stop the stream.

---
Developed by **Komal Kumar Kurapati**