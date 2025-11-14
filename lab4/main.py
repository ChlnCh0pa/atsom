import cv2
import numpy as np
print(cv2.__version__)
def get_angle_number(Gx, Gy, tg):
    if (Gx < 0):
        if (Gy < 0):
            if (tg > 2.414): return 0
            elif (tg < 0.414): return 6
            elif (tg <= 2.414): return 7
        else:
            if (tg < -2.414): return 4
            elif (tg < -0.414): return 5
            elif (tg >= -0.414): return 6
    else:
        if (Gy < 0):
            if (tg < -2.414): return 0
            elif (tg < -0.414): return 1
            elif (tg >= -0.414): return 2
        else:
            if (tg < 0.414): return 2
            elif (tg < 2.414): return 3
            elif (tg >= 2.414): return 4

def main(path, standart_deviation, kernel_size, porog):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("GrayImage", image)
    gaussianBlur = cv2.GaussianBlur(image, (kernel_size, kernel_size), standart_deviation)
    cv2.imshow("GaussianBlurImage", gaussianBlur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    length = np.zeros(gaussianBlur.shape)
    angle = np.zeros(gaussianBlur.shape)

    for x in range(1, (len(gaussianBlur) - 1)):
        for y in range(1, len(gaussianBlur[0]) - 1):
            Gx = (gaussianBlur[x + 1][y + 1] - gaussianBlur[x - 1][y - 1] +
                  gaussianBlur[x + 1][y - 1] - gaussianBlur[x - 1][y + 1] +
                  2 * (gaussianBlur[x + 1][y] - gaussianBlur[x - 1][y]))
            Gy = (gaussianBlur[x + 1][y + 1] - gaussianBlur[x - 1][y - 1] +
                  gaussianBlur[x - 1][y + 1] - gaussianBlur[x + 1][y - 1] +
                  2 * (gaussianBlur[x][y + 1] - gaussianBlur[x][y - 1]))
            length[x][y] = np.sqrt(Gx**2 + Gy**2)
            tg = np.arctan(Gy / Gx)
            print(Gx, Gy, length[x][y])
            get_angle_number(Gx, Gy, tg)

    cv2.imshow("Length", length)
    cv2.imshow("Angle", angle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    maxLen = np.max(length)
    borders = np.zeros(gaussianBlur.shape)
    for x in range(1, len(gaussianBlur) - 1):
        for y in range(1, len(gaussianBlur[0]) - 1):
            ix = 0
            iy = 0
            if (angle[x][y] == 0): iy = -1
            if (angle[x][y] == 1):
                iy = -1
                ix = 1
            if (angle[x][y] == 2): ix = 1
            if (angle[x][y] == 3):
                iy = 1
                ix = 1
            if (angle[x][y] == 4): iy = 1
            if (angle[x][y] == 5):
                iy = 1
                ix = -1
            if (angle[x][y] == 6): ix = -1
            if (angle[x][y] == 7):
                iy = -1
                ix = -1

            border = length[x][y] > length[x + ix][y + iy] and length[x][y] > length[x - ix][y - iy]
            borders[x][y] = 255 if border else 0
    cv2.imshow("Borders", borders)
    low_level = maxLen // porog
    high_level = maxLen // porog

    for x in range(1, len(gaussianBlur) - 1):
        for y in range(1, len(gaussianBlur[0]) - 1):
            if ((borders[x][y] == 255) and (length[x][y] < low_level)): borders[x][y] = 0

    for x in range(1, len(gaussianBlur) - 1):
        for y in range(1, len(gaussianBlur[0]) - 1):
            if ((borders[x][y] == 255) and (length[x][y] <= high_level)):
                if (borders[x - 1][y - 1] == 255 or borders[x - 1][y] == 255 or borders[x - 1][y + 1] == 255 or borders[x][y + 1] == 255 or borders[x + 1][y + 1] == 255 or borders[x + 1][y] == 255 or borders[x + 1][y - 1] == 255 or borders[x][y - 1] == 255): borders[x][y] = 255
                else: borders[x][y] = 0

    cv2.imshow("TwoBordersFilter", borders)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main("C:/Users/123/Desktop/acom/l4/lbo4tBsSzHE.jpg", 100, 5, 1)
