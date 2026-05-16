import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("image.png", 0)

# Add a check for successful image loading
if image is None:
    print("Error: image.png not found. Cannot proceed.")
else:
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Convert to absolute values (for display, as Sobel output can be negative)
    sobel_y_display = cv2.convertScaleAbs(sobel_y)

    cv2_imshow(image)
    cv2_imshow(sobel_y_display)

