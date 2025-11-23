# **Handeck**

A real-time hand-tracking mouse controller powered by OpenCV and MediaPipe. Control your entire mouse using nothing but your hand: move the cursor, click, double-click, right-click, and scroll — all through simple gestures.

## 🚀 Features

* Real-time hand tracking
* Cursor movement
* Left click / Double click
* Right click
* Scroll up & down
* Runs completely offline

## 🛠 Tech Stack

* **Python**
* **OpenCV**
* **MediaPipe**
* **PyAutoGUI** (or whatever you used for actual mouse events)

## 📦 Installation

```bash
git clone https://github.com/<your-username>/handeck.git
cd handeck
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python main.py
```

Move your hand in front of the camera and use the defined gestures.

## 🧠 How It Works

* MediaPipe detects hand landmarks
* Gesture logic interprets finger positions
* PyAutoGUI (or similar) triggers mouse events
* OpenCV handles video capture & visualization

## 🗂 Project Structure

```
/handeck
 ├── main.py
 ├── requirements.txt
 ├── gestures.py
 ├── controller.py
 └── README.md
```

## 📖 License

MIT License — use it however you want.
ably don't)
