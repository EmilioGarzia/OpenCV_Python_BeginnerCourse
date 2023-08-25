# OpenCV - Read every frame from video file
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-v", "--video", required=True, help="Insert the path of the video")
args = vars(parser.parse_args())

# Load the video
video = cv.VideoCapture(args["video"])

while video.isOpened():
    # read the frame from video, read() method return two value ret (for check the correctly read) and frame (the frame of the video)
    ret, frame = video.read()

    # The program terminate if the video is over or the user type "q" on the keyboard
    if not ret or cv.waitKey(1) & 0xFF == ord("q"):
        break
    
    # show one frame every 25 milliseconds
    cv.imshow("Video", frame)
    cv.waitKey(25)

# When programm is finish release the resource (video)
video.release()