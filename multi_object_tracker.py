# USAGE
# python multi_object_tracking.py --video videos/soccer_01.mp4 --tracker csrt

# import the necessary packages
import time
import cv2
import sys

# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[2]

if int(minor_ver) < 3:
    tracker_class = cv2.Tracker_create(tracker_type)
else:
    if tracker_type == 'BOOSTING':
        tracker_class = cv2.TrackerBoosting_create
    elif tracker_type == 'MIL':
        tracker_class = cv2.TrackerMIL_create
    elif tracker_type == 'KCF':
        tracker_class = cv2.TrackerKCF_create
    elif tracker_type == 'TLD':
        tracker_class = cv2.TrackerTLD_create
    elif tracker_type == 'MEDIANFLOW':
        tracker_class = cv2.TrackerMedianFlow_create
    # elif tracker_type == 'GOTURN':
    #     tracker = cv2.TrackerGOTURN_create()
    elif tracker_type == 'MOSSE':
        tracker_class = cv2.TrackerMOSSE_create
    elif tracker_type == "CSRT":
        tracker_class = cv2.TrackerCSRT_create

# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()

# if a video path was not supplied, grab the reference to the web cam
video = cv2.VideoCapture('videos/video.mp4')
if not video.isOpened():
    print("Could not open video")
    sys.exit()

# loop over frames from the video stream
while True:
    # grab the current frame, then handle if we are using a
    # VideoStream or VideoCapture object
    ok, frame = video.read()

    # check to see if we have reached the end of the stream
    if ok is None or frame is None:
        break

    # resize the frame (so we can process it faster)
    frame = cv2.resize(frame, (720, 640))

    # grab the updated bounding box coordinates (if any) for each
    # object that is being tracked
    success, boxes = trackers.update(frame)

    # loop over the bounding boxes and draw then on the frame
    if success:
        for bbox in boxes:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        box = cv2.selectROI("Frame", frame, fromCenter=False,
                            showCrosshair=True)

        # create a new object tracker for the bounding box and add it
        # to our multi-object tracker
        tracker = tracker_class()
        trackers.add(tracker, frame, box)

    # if the `q` key was pressed, break from the loop
    elif key == ord("q"):
        break

# if we are using a webcam, release the pointer
video.release()

# close all windows
cv2.destroyAllWindows()
