import cv2
from google.colab.patches import cv2_imshow
import numpy as np

print("Perform Sharpening of Image using Laplacian Mask with Positive Center Coefficient")

image = cv2.imread("img28.jpg", 0)

if image is None:
    print("Error: img28.jpg not found.")
else:
    kernel = np.array([[0, 1, 0],
                       [1, -5, 1],
                       [0, 1, 0]])

    sharpened = cv2.filter2D(image, -1, kernel)

    print("Original Image")
    cv2_imshow(image)

    print("Sharpened Image")
    cv2_imshow(sharpened)
