import cv2
img1 = cv2.imread(r'C:/Users/123/Desktop/acom/l1/lbo4tBsSzHE.jpg')
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.namedWindow('Sabaka', cv2.WINDOW_NORMAL)
cv2.namedWindow('Sabaka v hsv', cv2.WINDOW_NORMAL)
cv2.imshow('Sabaka', img1)
cv2.imshow('Sabaka v hsv', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

