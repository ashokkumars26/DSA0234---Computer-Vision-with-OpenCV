import cv2
from google.colab.patches import cv2_imshow

# Read image
img = cv2.imread('image.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display
cv2_imshow(img)
cv2_imshow(edges)
