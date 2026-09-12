import cv2
import numpy as np

img = cv2.imread("input12.jpg", 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

shift = np.fft.fftshift(dft)

print("Image shape:", img.shape)
print("DFT shape:", dft.shape)
print("Shifted DFT shape:", shift.shape)

mag = cv2.magnitude(shift[:,:,0], shift[:,:,1])
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow("Original", img)
cv2.imshow("DFT", mag)

cv2.imwrite("output.png", mag)

cv2.waitKey(0)
cv2.destroyAllWindows()