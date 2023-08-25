# OpenCV - Rotate the image with rotate() method
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert path of the image")
args = vars(parser.parse_args())

# Read the image from command line
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Rotate image with rotate() method
rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

# Show the image
cv.imshow("Original Image", img)
cv.imshow("Rotated Image", rotated)
cv.waitKey(0)