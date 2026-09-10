import cv2
import numpy as np

img = cv2.imread(r"C:\users\shyam it services\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2026-06-13 at 10.33.51 PM.jpeg", 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
  