import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input4.jpg", 0)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

print("Highest frequency:", hist.argmax())

plt.figure()
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.savefig("output.png")

cv2.imshow("Original Image", img)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()