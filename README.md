# Real-Time Hand Gesture Finger Counter Web Application 🖐️💻

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge)

A full-stack Computer Vision web application built with **Python, OpenCV, CVZone (MediaPipe), and Flask**. The system performs real-time hand landmark tracking, detects individual finger states (open/closed) using geometric spatial logic, and streams live calculation analytics to a web interface.

---

## ✨ Features

* **Real-time Hand Tracking**: Uses MediaPipe/CVZone to map 21 3D hand keypoints with low latency.
* **Dual-Hand Support**: Tracks both Left and Right hands simultaneously up to a total count of 10.
* **Geometric Spatial Logic**: Evaluates $X$ and $Y$ landmark pixel coordinates dynamically instead of relying on rigid classifications.
* **Flask Web Streaming**: Uses Multipart Video Streaming (MJPEG) to deliver a responsive live camera feed to the browser.
* **Interactive Dashboard**: Displays live differential statistics ($R:5 + L:5 = 10$) on an asynchronous overlay panel.

---

## 🛠️ Tech Stack

* **Language**: Python
* **Computer Vision**: OpenCV, CVZone / MediaPipe
* **Web Framework**: Flask (Jinja2, MJPEG Streaming)
* **Frontend**: HTML5, CSS3, JavaScript (Fetch API)

---

## 📂 Project Structure

```text
Finger_Detection_System/
│
├── app.py                 # Main Flask Application & Computer Vision Logic
├── requirements.txt       # Project Dependencies
├── README.md              # Project Documentation
└── templates/
    └── index.html         # Web Application Frontend Layout
