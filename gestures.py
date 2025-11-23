GESTURES = {
    (1, 1, 1, 1, 1): "palm",
    (1, 0, 0, 0, 0): "thumb",
    (0, 0, 0, 0, 1): "pinky",
    (0, 0, 0, 0, 0): "wrist",
    (0, 1, 0, 0, 0): "pointing",
    (0, 1, 1, 0, 0): "v_shaped",
    (1, 1, 0, 0, 1): "spiderman",
    (0, 1, 1, 1, 1): "4 fingers",
    (1, 1, 1, 0, 0): "first 3 fingers",
    (0, 1, 1, 1, 0): "middle 3 fingers",
    (0, 0, 1, 1, 1): "last 3 fingers",
    (1, 1, 0, 0, 0): "first 2 fingers",
    (0, 0, 1, 1, 0): "middle 2 fingers",
    (0, 0, 0, 1, 1): "last 2 fingers",
}

def current_gesture(handLms, label):
    fingers = {}

    lm = handLms.landmark

    if label == "Right":
        fingers["thumb"] = lm[4].x < lm[3].x
    elif label == "Left":
        fingers["thumb"] = lm[4].x > lm[3].x

    fingers["index"] = lm[8].y < lm[6].y
    fingers["middle"] = lm[12].y < lm[10].y
    fingers["ring"] = lm[16].y < lm[14].y
    fingers["pinky"] = lm[20].y < lm[18].y

    pattern = tuple(
        int(fingers[finger]) for finger in ["thumb", "index", "middle", "ring", "pinky"]
    )

    return GESTURES.get(pattern, "unknown")
