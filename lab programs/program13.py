import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("inp5.png", 0)

# Add a check for successful image loading
if image is None:
    print("Error: inp5.png not found. Cannot proceed.")
else:
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    
    # Convert to absolute values (for display, as Sobel output can be negative)
    sobel_x_display = cv2.convertScaleAbs(sobel_x)

    cv2_imshow(image)
    cv2_imshow(sobel_x_display)

