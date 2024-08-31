# Object-Detecion-System
This project demonstrates real-time object detection using a pre-trained YOLOv5 model. It captures video from a webcam or video file, detects objects in the video stream, and displays the results with bounding boxes and labels. Additionally, it saves every 10th frame with detected objects to a local directory.

## Requirements

- Python 3.12
- PyTorch
- OpenCV
- Ultralytics YOLOv5

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Cody-Alexander/Object-Detection-System.git
   cd object_detection
   ```
**Create and Activate a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
**Install Dependencies:**


## Usage
Run the main script to start real-time object detection:

```bash
python main.py
```
The video stream will display in a window with detected objects highlighted. Press the 'q' key to quit. Frames with detected objects will be saved in the frames directory.

## Troubleshooting
- Import Errors: Ensure all dependencies are installed correctly. Reinstall them if necessary.
- Attribute Errors: Make sure you are using the correct version of YOLOv5. Check the YOLOv5 documentation for any recent changes.

## Acknowledgments
- Ultralytics YOLOv5 for the pre-trained object detection model.
- OpenCV for real-time video processing.
- PyTorch for deep learning framework.
