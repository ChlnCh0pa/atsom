import cv2
import numpy as np

video = cv2.VideoCapture(0)
ok, img = video.read()
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter("video_s_krestom_zaliv123.avi", fourcc, 25, (w, h))
RED_RGB = (255, 0, 0)
GREEN_RGB = (0, 255, 0)
BLUE_RGB = (0, 0, 255)

COLORS_RGB = {
    "red": RED_RGB,
    "green": GREEN_RGB,
    "blue": BLUE_RGB
}

def bgr_to_rgb(bgr):
    return (bgr[2], bgr[1], bgr[0])

def get_closest_color_rgb(center_pixel_bgr):
    center_pixel_rgb = bgr_to_rgb(center_pixel_bgr)
    min_dist = float('inf')
    closest_color_rgb = RED_RGB

    for name, color_rgb in COLORS_RGB.items():
        dist = np.sqrt(sum((np.array(center_pixel_rgb) - np.array(color_rgb)) ** 2))
        if dist < min_dist:
            min_dist = dist
            closest_color_rgb = color_rgb
    return (closest_color_rgb[2], closest_color_rgb[1], closest_color_rgb[0])

while True:
    ok, img = video.read()
    if not ok:
        break

    h, w = img.shape[:2]
    center_x, center_y = w // 2, h // 2
    center_pixel_bgr = img[center_y, center_x]
    color = get_closest_color_rgb(center_pixel_bgr)
    thickness = -1
    goriz_width = 170
    goriz_height = 35
    ver_width = 35
    ver_total_height = 110

    goriz_top = center_y - goriz_height // 2
    goriz_bot = center_y + goriz_height // 2
    goriz_left = center_x - goriz_width // 2
    goriz_right = center_x + goriz_width // 2
    ver_top_top = center_y - ver_total_height
    ver_top_bot = goriz_top
    ver_left = center_x - ver_width // 2
    ver_right = center_x + ver_width // 2
    ver_bot_top = goriz_bot
    ver_bot_bot = center_y + ver_total_height

    cv2.rectangle(img, (goriz_left, goriz_top), (goriz_right, goriz_bot), color, thickness)
    cv2.rectangle(img, (ver_left, ver_top_top), (ver_right, ver_top_bot), color, thickness)
    cv2.rectangle(img, (ver_left, ver_bot_top), (ver_right, ver_bot_bot), color, thickness)

    video_writer.write(img)
    cv2.imshow('Krestik', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
video_writer.release()
cv2.destroyAllWindows()