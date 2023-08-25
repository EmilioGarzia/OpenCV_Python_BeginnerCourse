# OpenCV - Change the encoding color of the image with cvtColor() method
#
# @auhor Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert path of the image")
args = vars(parser.parse_args())

# Read the image (default encoding is BGR if you use IMREAD_COLOR)
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Change the encoding in only one channel (gray scale)
grayscale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Show the images
cv.imshow("Original Image (BGR)", img)
cv.imshow("Gray Image (GRAYSCALE)", grayscale_image)
cv.waitKey(0)