import argparse
import sys
import time
import imutils
from imutils.video import WebcamVideoStream
import cv2
import json
import datetime
import os
import csv


def main(args):
    frame_interval = 3  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0

    rtsp = 'rtsp://admin:fptai123@169.254.95.20/h265/ch1/main/av_stream'
    video_capture = WebcamVideoStream(rtsp).start()
    start_time = time.time()

    if args.debug:
        print("Debug enabled")
        # Get urls from .txt file

    while True:
        # Capture frame-by-frame
        frame = video_capture.read()
        frame = imutils.resize(frame, width=800)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.stop()
    cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        help='Enable some debug outputs.')
    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
