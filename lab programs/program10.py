import cv2
import numpy as np

image = cv2.imread("sample.jpg")

rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

pts2 = np.float32([[10, 100],
                   [280, 50],
                   [80, 280],
                   [300, 300]])

homography_matrix, status = cv2.findHomography(pts1, pts2)

transformed_image = cv2.warpPerspective(image, homography_matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformation", transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
