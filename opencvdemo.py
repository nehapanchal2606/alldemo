# import cv2
#
# im = cv2.imread(r'color.jpg')
# cv2.imshow('Original Image', im)
# cv2.imshow('Blurred Image', cv2.blur(im, (6, 6)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread(r'color.jpg', 1)
#
# kernel = np.ones((5, 5), np.float32) / 25
# blur = cv2.bilateralFilter(img, 9, 75, 75)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(blur), plt.title('Bilateral Filter')
# plt.xticks([]), plt.yticks([])
# cv2.imshow("Image", blur)


import cv2
img  = cv2.imread(r'page.png',1)
retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)
cv2.imshow("Original Image", img)
cv2.imshow("Threshold",threshold)
cv2.waitKey(0)