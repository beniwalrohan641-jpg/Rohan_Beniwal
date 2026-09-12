import cv2

img = cv2.imread("input8.jpg")

out = cv2.medianBlur(img, 5)

cv2.imshow("Input", img)
cv2.imshow("Median Filter", out)

cv2.imwrite("output.png", out)

cv2.waitKey(0)
cv2.destroyAllWindows()