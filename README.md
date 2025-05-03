
# 🤖 3D Printed Robotic Hand with Gesture Recognition

This project demonstrates a **low-cost, 3D-printed robotic hand** that responds to real-time hand gestures using computer vision. It uses **MediaPipe** and **OpenCV** in Python for gesture detection, and an **Arduino** to control servo motors based on the detected gestures.

---

## 📸 How It Works

1. **MediaPipe** detects hand landmarks using your webcam.
2. Gestures are converted into binary commands (e.g., `10100`).
3. Commands are sent via **Serial (USB)** to an **Arduino Uno**.
4. Arduino moves **servo motors** attached to the robotic fingers.

---

## 🛠️ Components

- Python 3
- OpenCV
- MediaPipe
- PySerial
- Arduino Uno
- Servo motors (x5)
- 3D-printed robotic hand parts

---

## 🔧 Setup

### Python Side (Mac/Windows/Linux)

```bash
# Install dependencies
pip install opencv-python mediapipe pyserial

# Run the gesture controller
python3 gesture_control.py
```

### Arduino Side

1. Open `gesture_hand.ino` in the Arduino IDE.
2. Connect your Arduino via USB.
3. Select the correct port and board.
4. Upload the code.

---

## 🧠 Gesture Mapping

Each finger is represented as:
- `1` = Finger Up
- `0` = Finger Down

Example: `10100` → Thumb and Middle Finger up, others down.

---



## 📂 File Structure

```
├── gesture_control.py     
├── gesture_hand.ino       
└── README.md              
```

---

## 📜 License

MIT License — feel free to use, modify, and share.

---

##  Author

**N. Vamshi Krishna Reddy**  
Graduate Student, Computer Science  
Auburn University at Montgomery

