import cv2
import numpy as np
from google.colab.patches import cv2_imshow 

image = cv2.imread("image.png")

if image is None:
    print("Error: image.png not found. Cannot proceed.")
else:
    rows, cols = image.shape[:2]

    matrix = np.float32([[1, 0, 100],
                         [0, 1, 50]])

    moved_image = cv2.warpAffine(image, matrix, (cols, rows))

    # Display images using cv2_imshow
    print("Original Image:")
    cv2_imshow(image)
    print("Moved Image:")
    cv2_imshow(moved_image)

