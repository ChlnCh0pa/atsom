import cv2
video = cv2.VideoCapture(0)
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
ok, img = video.read()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter("video_s_kameri_.avi", fourcc, 25, (w, h))
while True:
    ok, img = video.read()
    if not ok:
        break
    cv2.imshow('Okno', img)
    video_writer.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()