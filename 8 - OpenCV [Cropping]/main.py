# OpenCV - Cropping the image
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

# Define the coordinates and the size of the region to crop
x = 150
y = 150
width = 150
height = 100

# Crop the image
cropped_img = img[y:y+height, x:x+width]

# Show all image
cv.imshow("Original Image", img)
cv.imshow("Cropped Image", cropped_img)

# Close all windows and the programm after typing any button
cv.waitKey(0)
cv.destroyAllWindows()