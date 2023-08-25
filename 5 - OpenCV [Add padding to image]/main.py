# OpenCV - Add padding to image
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert path of the image")
args = vars(parser.parse_args())

# Read the image
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Add Padding to image
padded_image = cv.copyMakeBorder(img, top=50, bottom=50, left=50, right=50, borderType=cv.BORDER_CONSTANT, value=(0,255,0))

cv.imshow("Original Image", img)
cv.imshow("Padded Image", padded_image)
cv.waitKey(0)



####### ABOUT INFORMATION #######
#
# To apply padding you must use copyMakeBorder() method, this methos needs of:
#   ° Source image
#   ° Top padding value
#   ° Bottom padding value
#   ° Left padding value
#   ° Right padding value
#   ° Border Type of padding, you can use one of the defined costant in OpenCV like BORDER_COSTANT, BORDER_DEFAULT, BORDER_ISOLATED, ecc.
#   ° Value properties is used to specify the color of the padding zone, in our case the padding have a green color
#  
##############################################################################################