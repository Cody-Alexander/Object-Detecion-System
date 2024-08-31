import logging
import cv2
import os

def setup_logging(level):
    """Setup logging configuration."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')

def save_frame(frame, frame_count):
    """Save a frame as an image."""
    os.makedirs('frames', exist_ok=True)
    filename = f'frames/frame_{frame_count:04d}.jpg'
    cv2.imwrite(filename, frame)
    logging.info(f'Frame saved: {filename}')
