import cv2
from google.colab.patches import cv2_imshow

# Read image
img = cv2.imread('image.png')

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (7, 7), 0)

# Display
cv2_imshow(img)
cv2_imshow(blur)
