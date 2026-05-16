import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("inp5.png")

if image is None:
    print("Error: inp5.png not found. Cannot proceed.")
else:
    rows, cols = image.shape[:2]

    pts1 = np.float32([[50, 50],
                       [200, 50],
                       [50, 200]])

    pts2 = np.float32([[10, 100],
                       [200, 50],
                       [100, 250]])

    matrix = cv2.getAffineTransform(pts1, pts2)

    affine_image = cv2.warpAffine(image, matrix, (cols, rows))

    # Display images using cv2_imshow
    print("Original Image:")
    cv2_imshow(image)
    print("Affine Transformed Image:")
    cv2_imshow(affine_image)

