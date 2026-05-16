import cv2
from google.colab.patches import cv2_imshow
import numpy as np

print("Perform Sharpening of Image using High-Boost Filtering")

image = cv2.imread("img28.jpg", 0)

if image is None:
    print("Error: img28.jpg not found.")
else:
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    mask = cv2.subtract(image, blurred)

    high_boost = cv2.addWeighted(image, 1.8, mask, 1, 0)

    print("Original Image")
    cv2_imshow(image)

    print("High-Boost Sharpened Image")
    cv2_imshow(high_boost)
