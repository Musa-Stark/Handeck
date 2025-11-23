from collections import deque
import numpy as np
import pyautogui
import math


history = deque(maxlen=8)
MIN_MOVE_SPEED = 0.001


def clicks(d_ti, d_tm, d_tp):
    if d_ti < 20:
        pyautogui.click()
    elif d_tm < 25 and d_ti < 50:
        pyautogui.rightClick()


def pointer_gesture_control(handLms, w, h, gesture_type):
    lm = handLms.landmark

    thumb_x = int(lm[4].x * w)
    thumb_y = int(lm[4].y * h)
    index_x = int(lm[8].x * w)
    index_y = int(lm[8].y * h)
    middle_x = int(lm[12].x * w)
    middle_y = int(lm[12].y * h)
    ring_x = int(lm[16].x * w)
    ring_y = int(lm[16].y * h)
    pinky_x = int(lm[20].x * w)
    pinky_y = int(lm[20].y * h)

    d_ti = int(math.hypot(thumb_x - index_x, thumb_y - index_y))
    d_tm = int(math.hypot(thumb_x - middle_x, thumb_y - middle_y))
    d_tr = int(math.hypot(thumb_x - ring_x, thumb_y - ring_y))
    d_tp = int(math.hypot(thumb_x - pinky_x, thumb_y - pinky_y))


    history.append((lm[0].x, lm[0].y))

    if len(history) < 2:
        return

    x_movement = history[0][0] - history[-1][0]
    y_movement = history[0][1] - history[-1][1]

    x_speed = abs(x_movement) / len(history)
    y_speed = abs(y_movement) / len(history)

    f_x = int(lm[0].x * w)
    f_y = int(lm[0].y * h)

    x = int(np.interp(f_x, [200, 500], [0, 1366]))
    y = int(np.interp(f_y, [200, 400], [0, 768]))

    # speed threshold
    if x_speed < MIN_MOVE_SPEED:
        x = None
    if y_speed < MIN_MOVE_SPEED:
        y = None

    if gesture_type == "wrist":
        return

    if d_ti < 25 and d_tm < 30 and d_tr < 30 and d_tp < 30:
        pyautogui.dragTo(x, y)
    elif d_ti < 20 or d_tm < 30 and d_tr > 30 and d_tp > 50:
        clicks(d_ti=d_ti, d_tm=d_tm, d_tp=d_tp)
    elif gesture_type == "middle 3 fingers":
        pyautogui.scroll(100)
    elif gesture_type == "v_shaped":
        pyautogui.scroll(-100)
    elif gesture_type == "palm":
        pyautogui.moveTo(x, y)
