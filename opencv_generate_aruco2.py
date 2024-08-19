import numpy as np
import cv2

# decide which dictionary is most suitable
arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

print("[INFO] generating ArUCo tag type DICT_5X5_50 with ID 87")
tag = np.zeros((300, 300), dtype="uint8")
cv2.aruco.generateImageMarker(arucoDict, 20, 300, tag)

cv2.imwrite("C:\Python Projects\ProjectMERC/marker.png", tag)
cv2.imshow("ArUCo Tag", tag)
cv2.waitKey(0)