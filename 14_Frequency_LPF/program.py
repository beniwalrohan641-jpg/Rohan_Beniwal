import cv2
import numpy as np

img = cv2.imread("input14.jpg", 0)

dft = np.fft.fftshift(cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT))

r, c = img.shape
mask = np.zeros((r, c, 2), np.uint8)
mask[r//2-30:r//2+30, c//2-30:c//2+30] = 1

out = cv2.idft(np.fft.ifftshift(dft * mask))
out = cv2.magnitude(out[:,:,0], out[:,:,1])

out = cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX)
cv2.imwrite("output14.png", np.uint8(out))

cv2.imshow("LPF Output", np.uint8(out))
cv2.waitKey(0)
cv2.destroyAllWindows()