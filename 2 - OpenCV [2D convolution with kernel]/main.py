# How to apply kernel with 2D convolution on a image
#
# @author Emilio Garzia

import argparse as ap
import cv2 as cv
import filter

#Init and Set arguments parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", help="Path of the image")
args = vars(parser.parse_args())

#Read and show image from command line
img = cv.imread(args["image"], cv.IMREAD_COLOR)
cv.imshow("Original Image", img)
cv.waitKey()

#Make kernel for blurring
mask = filter.mean_blurring(9)
filtered_image = cv.filter2D(src=img, ddepth=-1, kernel=mask, anchor=(-1,-1), delta=0)

#Show the image with filter
cv.imshow("Filtered Image", filtered_image)
cv.waitKey()