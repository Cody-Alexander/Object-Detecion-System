import torch

class ObjectDetector:
    def __init__(self, model_name='yolov5s', pretrained=True):
        """Initialize the object detector with a pre-trained model."""
        self.model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=pretrained)
        self.model.eval()  # set the model to evaluation mode

    def detect_objects(self, frame):
        """Detect objects in a given frame."""
        results = self.model(frame)
        return results
