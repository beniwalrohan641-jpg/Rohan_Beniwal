import cv2

img = cv2.imread("input7.jpg")

# 5x5 odd kernel for smooth Gaussian filtering
out = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("Input", img)
cv2.imshow("Gaussian Filter", out)

cv2.imwrite("output.png", out)

cv2.waitKey(0)
cv2.destroyAllWindows()