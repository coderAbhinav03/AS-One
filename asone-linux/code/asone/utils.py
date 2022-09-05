from asone.detectors import YOLOv5Detector
from asone.detectors import YOLOv7Detector
from asone.detectors import YOLOv6Detector
from asone.trackers import ByteTrack
from asone.trackers import NorFair

detectors={
    'yolov5s' : YOLOv5Detector,
    'yolov7' : YOLOv7Detector,
    'yolov6' : YOLOv6Detector
}

trackers={
    'byte_track' : ByteTrack,
    'norfair': NorFair
}


def get_detector(detector, use_cuda=True, use_onnx=False):
    detector = detectors.get(detector, None)

    if detector is not None:
        return detector(use_cuda=use_cuda, use_onnx=use_onnx)
    else:
        return None

def get_tracker(tracker, detector, use_cuda=True, use_onnx=False):
    tracker = trackers.get(tracker, None)

    if tracker is not None:
        return tracker(detector)
    else:
        return None

