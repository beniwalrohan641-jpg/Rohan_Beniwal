
import cv2
import numpy as np

img = cv2.imread("input3.jpg", 0)

mn = np.min(img)
mx = np.max(img)

out = ((img - mn) * 255 / (mx - mn)).astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("Contrast Stretched", out)

cv2.imwrite("output.png", out)

cv2.waitKey(0)
cv2.destroyAllWindows()