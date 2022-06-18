import cv2

from matplotlib import pyplot

imaging = cv2.imread("post.png")
img_gray = cv2.cvtColor(imaging, cv2.COLOR_RGB2GRAY)
imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)

pyplot.subplot(1, 1, 1)

pyplot.imshow(imaging_rgb)
pyplot.show()
