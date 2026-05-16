import cv2
from google.colab.patches import cv2_imshow
import numpy as np

print("Perform Sharpening of Image using Gradient Masking")

image = cv2.imread("img28.jpg", 0)

if image is None:
    print("Error: img28.jpg not found.")
else:
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    gradient = cv2.magnitude(grad_x, grad_y)

    gradient = np.uint8(gradient)

    sharpened = cv2.add(image, gradient)

    print("Original Image")
    cv2_imshow(image)

    print("Gradient Masked Sharpened Image")
    cv2_imshow(sharpened)
