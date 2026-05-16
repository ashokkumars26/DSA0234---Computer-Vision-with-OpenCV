import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("img28.jpg", 0)

# Add a check for successful image loading
if image is None:
    print("Error: img28.jpg not found. Cannot proceed.")
else:
    edges = cv2.Canny(image, 100, 200)

    cv2_imshow(image)
    cv2_imshow(edges)

