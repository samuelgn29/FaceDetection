# Webcam Face Detection with OpenCV

A simple real-time face detection project using Python and OpenCV.  
The program captures video from your webcam, applies preprocessing, and detects faces with Haarcascades.  
Bounding boxes and FPS (frames per second) are displayed live.

---

## 📂 Project Structure
FaceDetection/

├── data/ # Saved screenshots

├── docs/ # Notes, evaluation

├── models/ # Haarcascade XML files

├── src/ # Python source code

│ ├── camera.py

│ ├── config.py

│ ├── main.py

│ ├── overlay.py

│ ├── processing.py

│ └── utils.py

└── README.md

---

## ⚙️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/DEIN_USERNAME/FaceDetection.git
   cd FaceDetection
2. Install dependencies:
    ```bash
   pip install opencv-python numpy

---

## ▶️ Usage
Run the program from the project root:

python src/main.py

---

## 📸 Example Output
Add a screenshot here later

---

## 📊 Features
Live webcam feed with FPS counter

Screenshot saving with timestamp

Preprocessing (grayscale, blur, histogram equalization)

Face detection with Haarcascade

Bounding boxes on detected faces

---

## ⚠️ Limitations
Works best with frontal faces in normal lighting

Haarcascade can be inaccurate with profiles, glasses, or low light

Only detects — does not recognize or track identities

---

# 📜 License
MIT License – feel free to use and adapt.



