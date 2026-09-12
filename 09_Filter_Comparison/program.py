import cv2

img = cv2.imread("input9.jpg")

mean = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (11,11), 0)
median = cv2.medianBlur(img, 5)

cv2.imshow("Mean", mean)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)

cv2.imwrite("output_mean.png", mean)
cv2.imwrite("output_gaussian.png", gaussian)
cv2.imwrite("output_median.png", median)

cv2.waitKey(0)
cv2.destroyAllWindows()