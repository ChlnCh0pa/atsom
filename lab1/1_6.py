import cv2

video = cv2.VideoCapture(0)
ok, img = video.read()
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter("video_s_krestom.avi", fourcc, 25, (w, h))

while True:
    ok, img = video.read()
    if not ok:
        break

    color = (0, 0, 255)
    thickness = 1
    h, w = img.shape[:2]
    center_x, center_y = w // 2, h // 2

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