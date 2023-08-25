# OpenCV - Flip the image
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set the parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert the path of the image")
args = vars(parser.parse_args())

# Read the image from command line
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Flip the image horizontally
horzizontally_flipped = cv.flip(img, 1)

# Flip the image vertically
vertically_flipped = cv.flip(img, 0)

# Show the output
cv.imshow("Original Image", img)
cv.imshow("Horizzontally Flipped", horzizontally_flipped)
cv.imshow("Vertically Flipped", vertically_flipped)
cv.waitKey(0)