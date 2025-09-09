import cv2
img1 = cv2.imread(r'C:\Users\123\Desktop\acom\l1\lbo4tBsSzHE.jpg',cv2.WINDOW_NORMAL """ cv2.IMREAD_REDUCED_GRAYSCALE_8, cv2.IMREAD_GRAYSCALE , cv2.IMREAD_REDUCED_COLOR_8 """)
cv2.namedWindow('Sabaka v kepke', cv2.WINDOW_NORMAL)
cv2.imshow('Sabaka v kepke', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()