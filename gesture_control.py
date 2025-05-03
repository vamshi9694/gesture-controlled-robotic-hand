
# gesture_control.py

import cv2
import serial
import mediapipe as mp
import time

# Set up serial communication with Arduino (update 'COM3' or '/dev/ttyUSB0' as needed)
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # wait for Arduino to initialize
except:
    arduino = None
    print("Warning: Could not connect to Arduino.")

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# Define finger tip indices
finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

# Gesture logic
def get_finger_status(hand_landmarks):
    status = []
    for tip in finger_tips:
        tip_y = hand_landmarks.landmark[tip].y
        pip_y = hand_landmarks.landmark[tip - 2].y
        status.append(1 if tip_y < pip_y else 0)  # 1 = Finger up, 0 = Finger down
    return status

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                status = get_finger_status(hand_landmarks)
                command = ''.join(map(str, status))  # e.g., "10100"
                cv2.putText(frame, f"Gesture: {command}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                if arduino:
                    arduino.write((command + '\n').encode())

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
