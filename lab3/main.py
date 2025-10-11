import cv2
import numpy as np
def Gauss(x, y, omega, a, b):
    m1 = 1 / (2 * np.pi * (omega ** 2))
    m2 = np.exp(-((x - a) ** 2 + (y - b) ** 2) / (2 * (omega ** 2)))
    return m1 * m2

def GaussianBlur(image, kernel_size, standart_deviation):
    kernel = np.ones((kernel_size, kernel_size))
    a = b = (kernel_size + 1) // 2

    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i, j] = Gauss(i, j, standart_deviation, a, b)
    print("Матрица ядра свертки для размера: ", kernel_size)
    print(kernel)

    summa = kernel.sum()
    kernel /= summa
    print("Нормализованная матрица ядра свертки: \n", kernel, "\n")

    imgBLur = image.copy()
    x_y_start = kernel_size // 2

    #
    for i in range(x_y_start, imgBLur.shape[0] - x_y_start):
        for j in range(x_y_start, imgBLur.shape[1] - x_y_start):
            val = 0


            for k in range(-x_y_start, x_y_start + 1):
                for l in range(-x_y_start, x_y_start + 1):
                    val += image[i + k, j + l] * kernel[k + x_y_start, l + x_y_start]
            imgBLur[i, j] = val
    return imgBLur

image = cv2.imread("C:/Users/123/Desktop/acom/l3/lbo4tBsSzHE.jpg", cv2.IMREAD_GRAYSCALE)

blur1 = GaussianBlur(image, 3, 100)
blur2 = GaussianBlur(image, 3, 10)
blur3 = GaussianBlur(image, 5, 100)
blur4 = GaussianBlur(image, 5, 10)
blur5 = GaussianBlur(image, 7, 100)
blur6 = GaussianBlur(image, 7, 10)

cv2.imshow("Original", image)
cv2.imshow("Kernel size 3 | Standart deviation 100", blur1)
cv2.imshow("Kernel size 3 | Standart deviation 10", blur2)
cv2.imshow("Kernel size 5 | Standart deviation 100", blur3)
cv2.imshow("Kernel size 5 | Standart deviation 10", blur4)
cv2.imshow("Kernel size 7 | Standart deviation 100", blur5)
cv2.imshow("Kernel size 7 | Standart deviation 10", blur6)

cv2.waitKey(0)
cv2.destroyAllWindows()

imageBlurInCv2 = cv2.GaussianBlur(image, (7, 7), 100)
cv2.imshow("CV2 |Kernel size 7 | Standart deviation 100 | CV2", imageBlurInCv2)
cv2.imshow("Kernel size 7 | Standart deviation 100", blur5)
cv2.waitKey(0)
cv2.destroyAllWindows()