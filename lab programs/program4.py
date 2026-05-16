import cv2
from google.colab.patches import cv2_imshow 

# Read the image
image = cv2.imread("image.png")   

if image is None:
    print("Error: Neither image.jpg nor image1b.png found. Cannot proceed.")
else:
    height, width = image.shape[:2]
…    cv2_imshow(bigger_image)
    print("Smaller Image:")
    cv2_imshow(smaller_image)
