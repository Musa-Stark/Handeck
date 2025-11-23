import cv2
import mediapipe as mp
from gestures import current_gesture
import pyautogui
from controller import pointer_gesture_control


pyautogui.FAILSAFE = False

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1, min_tracking_confidence=0.7, min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Error while reading...")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rbg_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rbg_frame)
    if results.multi_hand_landmarks:
        for handLms, handedness in zip(
            results.multi_hand_landmarks, results.multi_handedness
        ):
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            label = handedness.classification[0].label

            gesture = current_gesture(handLms, label)
            if gesture:
                pointer_gesture_control(handLms, w, h, gesture)

    # cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
