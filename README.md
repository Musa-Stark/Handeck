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
* **PyAutoGUI**

## 📦 Installation

```bash
git clone https://github.com/Musa-Stark/Handeck.git
cd Handeck
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
* PyAutoGUI triggers mouse events
* OpenCV handles video capture & visualization

## ✋ Gesture Controls
| Gesture                                         | Action                  |
| ----------------------------------------------- | ----------------------- |
| **Palm (all fingers up)**                       | Move cursor             |
| **Wrist (all fingers down)**                    | Disable cursor movement |
| **Thumb + Index touching**                      | Left Click              |
| **Thumb + Middle touching**                     | Right Click             |
| **V-Shaped (index + middle up)**                | Scroll Down             |
| **Middle 3 Fingers (index + middle + ring up)** | Scroll Up               |


## 🗂 Project Structure

```
/Handeck
 ├── main.py
 ├── requirements.txt
 ├── gestures.py
 ├── controller.py
 └── README.md
```

## 📖 License

MIT License — use it however you want.
