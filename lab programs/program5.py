import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow

image = cv2.imread("inp5.png")

if image is None:
    print("Error: inp5.png not found. Cannot proceed.")
else:
    clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display images using cv2_imshow
    print("Original Image:")
    cv2_imshow(image)
    print("Clockwise Rotation:")
    cv2_imshow(clockwise)
    print("Counter Clockwise Rotation:")
    cv2_imshow(counter_clockwise)

    # cv2.waitKey(0) and cv2.destroyAllWindows() are not needed with cv2_imshow
