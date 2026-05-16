import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("img28.jpg")

if image is None:
    print("Error: img28.jpg not found. Cannot proceed.")
else:
    rows, cols = image.shape[:2]

    pts1 = np.float32([[50, 50],
                       [300, 50],
                       [50, 300],
                       [300, 300]])

    pts2 = np.float32([[10, 100],
                       [280, 50],
                       [80, 280],
                       [300, 300]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    dlt_image = cv2.warpPerspective(image, matrix, (cols, rows))

    cv2_imshow(image)
    cv2_imshow(dlt_image)

