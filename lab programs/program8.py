import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("image1e.png") # Changed from .jpg to .png

if image is None:
    print("Error: image1e.png not found. Cannot proceed.")
else:
    rows, cols = image.shape[:2]

    pts1 = np.float32([[50, 50],
                       [300, 50],
                       [50, 300],
                       [300, 300]])

    pts2 = np.float32([[10, 100],
                       [300, 50],
                       [100, 250],
                       [300, 300]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

    cv2_imshow(image) 
    cv2_imshow(perspective_image) 
