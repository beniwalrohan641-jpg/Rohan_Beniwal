import cv2
import numpy as np

img = cv2.imread("input15.jpg", 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft = np.fft.fftshift(dft)

r, c = img.shape
mask = np.ones((r, c, 2), np.uint8)
mask[r//2-20:r//2+20, c//2-20:c//2+20] = 0

dft = dft * mask
dft = np.fft.ifftshift(dft)

out = cv2.idft(dft)
out = cv2.magnitude(out[:,:,0], out[:,:,1])
out = cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow("HPF", np.uint8(out))
cv2.imwrite("output.png", np.uint8(out))

cv2.waitKey(0)
cv2.destroyAllWindows()