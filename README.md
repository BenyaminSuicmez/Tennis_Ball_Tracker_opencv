# Tennis Ball Tracker

Live color-based object tracking using OpenCV. Detects a tennis ball 
through a webcam feed using HSV color segmentation and highlights it 
with a bounding box in real time.

## How it works

1. Each camera frame is converted to HSV color space
2. `cv2.inRange()` isolates pixels matching the ball's measured color range
3. Contours are extracted from the resulting mask
4. The largest contour above a minimum size threshold is tracked
5. A bounding box and label are drawn around the detected ball

## Demo

### Locked on ball
<img width="956" height="559" alt="Bildschirmfoto 2026-08-20 um 18 58 12" src="https://github.com/user-attachments/assets/e4ea4ae2-bd83-4945-aade-47906e546adb" />

### Searching state
<img width="956" height="559" alt="Bildschirmfoto 2026-08-20 um 18 57 38" src="https://github.com/user-attachments/assets/33a9c03f-9265-4f2d-8099-92d83e528ba7" />


## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Press `q` to quit.

## Notes

- HSV color range was manually calibrated for the specific ball/lighting 
  used, via a separate click-to-sample tool
- A minimum bounding-box size filter prevents false positives (e.g. hair, 
  small color-matched objects)
