import cv2
from google.colab.patches import cv2_imshow
import numpy as np

print("Perform Sharpening of Image using Unsharp Masking")

image = cv2.imread("img28.jpg", 0)

if image is None:
    print("Error: img28.jpg not found.")
else:
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

    print("Original Image")
    cv2_imshow(image)

    print("Sharpened Image")
    cv2_imshow(sharpened)
