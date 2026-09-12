import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input5.jpg", 0)

equalized = cv2.equalizeHist(img)

cv2.imshow("Original", img)
cv2.imshow("Equalized", equalized)

cv2.imwrite("output.png", equalized)

plt.figure()

plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Before")

plt.subplot(1, 2, 2)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("After")

plt.savefig("histogram_comparison.png")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()