# carify_circle.py
# Babaguhin ang pinakamalaking bilog sa bawat frame ng video papuntang isang simpleng cartoon na kotse.
# Output: ./output_carified.mp4

import cv2
import numpy as np
from pathlib import Path

# Palitan ito kung ibang path ang video
INPUT_VIDEO = Path("579136550_25084497551172597_5099691762038110279_n.mp4")
OUTPUT_VIDEO = Path("output_carified.mp4")

if not INPUT_VIDEO.exists():
    raise FileNotFoundError(f"Input video not found at {INPUT_VIDEO.resolve()}")

cap = cv2.VideoCapture(str(INPUT_VIDEO))
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(str(OUTPUT_VIDEO), fourcc, fps, (w, h))

frame_idx = 0
print("Starting processing...")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    display = frame.copy()

    # Convert to gray and blur to help circle detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)

    # Hough Circle detection (tweak params if needed)
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT,
                               dp=1.2, minDist=50,
                               param1=100, param2=30,
                               minRadius=10, maxRadius=0)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        # Piliin ang pinakamalaking bilog (malamang siya ang "target")
        cx, cy, r = max(circles, key=lambda c: c[2])

        # Gumawa ng overlay para semi-transparent painting
        overlay = display.copy()

        # Car body (relative sa radius ng bilog)
        body_w = int(2.4 * r)
        body_h = int(0.9 * r)
        body_x1 = int(cx - body_w // 2)
        body_y1 = int(cy - int(0.6 * r))
        body_x2 = body_x1 + body_w
        body_y2 = body_y1 + body_h

        # Clamp values to frame bounds
        body_x1 = max(0, body_x1); body_y1 = max(0, body_y1)
        body_x2 = min(w - 1, body_x2); body_y2 = min(h - 1, body_y2)

        # Draw car body (filled rectangle) - red
        cv2.rectangle(overlay, (body_x1, body_y1), (body_x2, body_y2), (0,0,255), -1)

        # Roof (trapezoid)
        roof_w = int(body_w * 0.6)
        roof_h = int(body_h * 0.5)
        roof_x1 = cx - roof_w // 2
        roof_y1 = body_y1 - roof_h + 5
        roof_x2 = roof_x1 + roof_w
        roof_y2 = roof_y1 + roof_h
        roof_pts = np.array([
            [roof_x1, roof_y2],
            [roof_x1 + int(roof_w * 0.15), roof_y1],
            [roof_x2 - int(roof_w * 0.15), roof_y1],
            [roof_x2, roof_y2]
        ], np.int32)
        cv2.fillPoly(overlay, [roof_pts], (0,0,200))

        # Window
        win_x1 = roof_x1 + int(roof_w*0.08)
        win_y1 = roof_y1 + int(roof_h*0.15)
        win_x2 = roof_x2 - int(roof_w*0.08)
        win_y2 = roof_y2 - int(roof_h*0.1)
        cv2.rectangle(overlay, (win_x1, win_y1), (win_x2, win_y2), (220,220,220), -1)

        # Wheels
        wheel_r = max(4, int(0.45 * r))
        wheel_offset_x = int(body_w * 0.28)
        wheel_y = body_y2 + int(wheel_r*0.2)
        left_wheel_center = (max(0, min(w-1, cx - wheel_offset_x)), max(0, min(h-1, wheel_y)))
        right_wheel_center = (max(0, min(w-1, cx + wheel_offset_x)), max(0, min(h-1, wheel_y)))
        cv2.circle(overlay, left_wheel_center, wheel_r, (20,20,20), -1)
        cv2.circle(overlay, right_wheel_center, wheel_r, (20,20,20), -1)

        # Headlight
        head_x = body_x2 - int(body_w*0.08)
        head_y = body_y1 + int(body_h*0.45)
        cv2.circle(overlay, (head_x, head_y), max(3, r//6), (0,255,255), -1)

        # Blend overlay (alpha)
        alpha = 0.95
        cv2.addWeighted(overlay, alpha, display, 1 - alpha, 0, display)

    # kung walang nakita, isusulat lang ang original frame
    out.write(display)
    frame_idx += 1
    if frame_idx % 100 == 0:
        print(f"Processed {frame_idx} frames...")

cap.release()
out.release()
print(f"Done. Output video saved to: {OUTPUT_VIDEO.resolve()}")
