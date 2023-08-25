# OpenCV - Manage Contrast and Brightness of the image
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

# Specify the value of contrast (alpha value) and brightness (beta value)
alpha = 1.5
beta = 60

# Apply that value to the image
new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

# Show the output
cv.imshow("Original Image", img)
cv.imshow("Modified Image", new_image)
cv.waitKey(0)


############## ABOUT INFORMATION ##############
#                                             #
#  alpha > 1 -> Increase the contrast         #
#  alpha = 1 -> Set the contrast to default   #
#  alpha < 1 -> Decrease the contrast         #
#                                             #
###############################################