import cv2
from google.colab.patches import cv2_imshow
import numpy as np

image = cv2.imread("img28.jpg", 0)

if image is None:
    print("Error: img28.jpg not found.")
else:
    sobel_xy = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=3)

    cv2_imshow(image)
    cv2_imshow(sobel_xy)
