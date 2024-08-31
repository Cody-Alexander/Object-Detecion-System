import cv2
import logging
from config import Config
from detector import ObjectDetector
from helper import setup_logging, save_frame

def main():
    # setup logging
    setup_logging(Config.LOG_LEVEL)
    
    # initialize object detector
    detector = ObjectDetector(model_name=Config.MODEL_NAME, pretrained=Config.PRETRAINED)
    
    # start video capture
    cap = cv2.VideoCapture(Config.VIDEO_SOURCE)
    
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            logging.warning('No frame received from video source')
            break

        # perform object detection
        results = detector.detect_objects(frame)
        
        # render results
        results.render()
        frame = results.ims[0]
        
        # display the frame
        cv2.imshow('YOLO Object Detection', frame)
        
        # save frame every 10th frame
        if frame_count % 10 == 0:
            save_frame(frame, frame_count)
        
        # quit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        frame_count += 1
    
    # release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
