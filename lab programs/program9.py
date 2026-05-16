import cv2
import numpy as np

video = cv2.VideoCapture("inpu4.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    rows, cols = frame.shape[:2]

    pts1 = np.float32([[50, 50],
                       [300, 50],
                       [50, 300],
                       [300, 300]])

    pts2 = np.float32([[10, 100],
                       [300, 50],
                       [100, 250],
                       [300, 300]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    perspective_video = cv2.warpPerspective(frame, matrix, (cols, rows))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", perspective_video)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
