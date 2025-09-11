import cv2
def read():
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_BRIGHTNESS, 0.27)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 140)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 50)
    video.set(cv2.CAP_PROP_SATURATION, 0.5)
    video.set(cv2.CAP_PROP_CONTRAST, 0.5)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH) )
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT) )
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.avi", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()
        cv2.imshow('CAM', img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == ord('z'):
            break

    video.release()
    video_writer.release()
    cv2.destroyAllWindows()

read()