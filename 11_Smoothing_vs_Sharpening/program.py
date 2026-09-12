import cv2
import numpy as np

img = cv2.imread("input11.jpg")

# Smoothing
smooth = cv2.GaussianBlur(img, (11, 11), 0)

# Sharpening
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Smooth", smooth)
cv2.imshow("Sharp", sharp)

cv2.imwrite("output_smooth.png", smooth)
cv2.imwrite("output_sharp.png", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()