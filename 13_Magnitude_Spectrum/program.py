import cv2
import numpy as np

img = cv2.imread("input13.jpg", 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
shift = np.fft.fftshift(dft)

mag = cv2.magnitude(shift[:,:,0], shift[:,:,1])
mag = 20 * np.log(mag + 1)

mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
mag = np.uint8(mag)

cv2.imshow("Original", img)
cv2.imshow("Magnitude Spectrum", mag)

cv2.imwrite("output.png", mag)

cv2.waitKey(0)
cv2.destroyAllWindows()