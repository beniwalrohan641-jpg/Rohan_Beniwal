import cv2
import numpy as np

img = cv2.imread(r"C:\Users\shyam it services\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2026-07-09 at 10.46.57 PM.jpeg")

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

Sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Sharpened Image", Sharp)

cv2.waitKey(0)
cv2.destroyAllWindows() 


