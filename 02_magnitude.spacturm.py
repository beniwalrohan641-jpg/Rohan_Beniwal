import cv2
import numpy as np

img = cv2.imread(r"C:\Users\shyam it services\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2026-07-12 at 11.24.33 PM.jpeg", 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

magnitude_spectrum = 20 * np.log(magnitude + 1)

spectrum = cv2.normalize(
    magnitude_spectrum,
    None,
    0,
    255,
    cv2.NORM_MINMAX,
    dtype=cv2.CV_8U
)
 
cv2.imshow("Original", img)
cv2.imshow("Spectrum Image", spectrum)

cv2.waitKey(0)
cv2.destroyAllWindows()