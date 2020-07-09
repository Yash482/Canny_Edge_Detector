import numpy as np
import cv2
import matplotlib.pyplot as plt
# matplotlib qt

img = cv2.imread("mobile.jpeg")
img_copy= np.copy(img)
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
#plt.imshow(img_copy)
gray = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY)
#plt.imshow(gray)

edged = cv2.Canny(gray, 120, 240)

plt.imshow(edged)