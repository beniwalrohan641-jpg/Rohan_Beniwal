import cv2
import numpy as np

img = cv2.imread("input6.jpg")

# 3x3 mean filter
small = np.ones((3, 3), np.float32) / 9
out1 = cv2.filter2D(img, -1, small)

# 7x7 mean filter
large = np.ones((7, 7), np.float32) / 49
out2 = cv2.filter2D(img, -1, large)

cv2.imshow("Original", img)
cv2.imshow("Mean Filter", out2)

cv2.imwrite("output.png", out2)

cv2.waitKey(0)
cv2.destroyAllWindows()