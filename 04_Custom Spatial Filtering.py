import cv2
import numpy as np

img  = cv2.imread("C:\\users\\shyam it services\\OneDrive\\Pictures\\optimus_prime_transformers_the_last_knight_hd.jpg", 0)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(img, -1, kernel)


cv2.imshow("Original", img)
cv2.imshow("Sharpening", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()