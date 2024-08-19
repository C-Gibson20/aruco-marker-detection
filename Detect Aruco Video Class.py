from imutils.video import VideoStream
import imutils
import time
import cv2

class Detection():

    def __init__(self):
        self.arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
        self.arucoParams = cv2.aruco.DetectorParameters()
        self.center = (None)
        self.allMarkers = {} 
        self.vs = VideoStream(src=0, resolution=(640, 400), framerate=60).start()
        time.sleep(0.5)

    def detection(self):
        self.frame = self.vs.read()
        self.frame = imutils.resize(self.frame, width=1000)
        (self.corners, ids, rejected) = cv2.aruco.detectMarkers(self.frame, self.arucoDict, parameters=self.arucoParams)

	
        if len(self.corners) > 0:
            ids = ids.flatten()
            for (markerCorner, markerID) in zip(self.corners, ids):
                self.corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = self.corners

                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))
			
                cv2.line(self.frame, topLeft, topRight, (0, 255, 0), 2)
                cv2.line(self.frame, topRight, bottomRight, (0, 255, 0), 2)
                cv2.line(self.frame, bottomRight, bottomLeft, (0, 255, 0), 2)
                cv2.line(self.frame, bottomLeft, topLeft, (0, 255, 0), 2)

                cv2.circle(self.frame, topRight, 4, (0, 0, 30), -1)
                cv2.circle(self.frame, topLeft, 4, (0, 0, 80), -1)
                cv2.circle(self.frame, bottomRight, 4, (0, 0, 130), -1)
                cv2.circle(self.frame, bottomLeft, 4, (0, 0, 180), -1)

                center_X = int((topLeft[0] + bottomRight[0]) / 2.0)
                center_Y = int((topLeft[1] + bottomRight[1]) / 2.0)
                self.allMarkers[markerID] = (center_X, center_Y)
                
                self.center = (center_X, center_Y)

                cv2.circle(self.frame, (center_X, center_Y), 4, (0, 0, 255), -1)

                cv2.putText(self.frame, str(markerID), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

if __name__ == "__main__":
    test = Detection()

    while True:
        test.detection()
        cv2.imshow("Frame", test.frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
