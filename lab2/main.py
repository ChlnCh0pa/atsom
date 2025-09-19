import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_channel = hsv[:, :, 0]
    h_colormap = cv2.applyColorMap(cv2.convertScaleAbs(h_channel, alpha=255/180), cv2.COLORMAP_HSV)
    cv2.imshow('HSV Hue Channel (Colormap)', h_colormap)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask1, mask2)
    cv2.imshow('Threshold (Red Filter)', mask_red)

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('After Morphology (Opening + Closing)', closing)

    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_frame = frame.copy()

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            x, y, w, h = cv2.boundingRect(largest_contour)
            left = cx - w // 2
            top = cy - h // 2
            right = cx + w // 2
            bottom = cy + h // 2
            cv2.rectangle(output_frame, (left, top), (right, bottom), (0, 0, 0), 2)
            cv2.circle(output_frame, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(output_frame, f'Area: {int(area)}', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('Original with Bounding Box', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()