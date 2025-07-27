# Aruco Marker Detection

This project utilizes OpenCV's `cv2.aruco` module to detect ArUco markers in both real-time video streams and static images. The implementation is modular and efficient, with extensible Python code suitable for robotics, augmented reality (AR), and computer vision research.

### ArUco Marker Detection

* **Dictionary:** The system uses the `DICT_5X5_50` predefined dictionary, which provides 50 unique 5×5 markers optimized for reliable detection in varied conditions.
* **Detector Configuration:** Marker detection is handled via `cv2.aruco.detectMarkers()`, with customizable parameters using `cv2.aruco.DetectorParameters()` to control detection sensitivity, corner refinement, and error correction.

### Real-Time Detection

* **Video Input:** Captures live video from the default webcam using `imutils.video.VideoStream`, enabling lightweight, cross-platform camera access.
* **Preprocessing:** Each frame is resized using `imutils.resize()` for consistent processing and improved performance.
* **Detection Workflow:**

  * ArUco markers are detected in the video frame.
  * Marker corners are extracted and reshaped to determine the four bounding points.
  * Bounding boxes are drawn around each marker using `cv2.line()`.
  * Marker IDs and corner points are annotated with visual indicators.
  * The center of each marker is computed and highlighted with a red dot.
* **Data Handling:** The system tracks detected marker IDs and their center coordinates using a dictionary (`self.allMarkers`), enabling downstream integration for tracking or spatial analysis.

### Static Image Detection 

* **Image Input:** Loads and processes a static image (`.png`, `.jpg`) containing ArUco markers.
* **Processing:** Follows the same detection pipeline as the video stream.
* **Output:**

  * Annotated image with marker IDs and centers.
  * Console output listing detected marker IDs for verification.

### Object-Oriented Design

The video detection script is structured around a `Detection` class, encapsulating:

* Frame acquisition and resizing
* Marker detection and annotation
* Real-time visualization
* Internal state tracking (e.g., `self.center`, `self.allMarkers`)

This modular design simplifies extension and integration into larger computer vision systems or robotics platforms.
