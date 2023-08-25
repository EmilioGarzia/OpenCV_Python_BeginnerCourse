# OpenCV - Resize the image
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Zoom by height function implementation
def zoom_by_height(src, new_height):
    h, w = src.shape[:2]   # calculate height and width of the source image
    aspect_ratio = h/w     # calculate the aspect ratio of the source image
    new_width = new_height * aspect_ratio
    return cv.resize(img, dsize=(new_height,int(new_width)), interpolation=cv.INTER_CUBIC)

# Zoom by width function implementation
def zoom_by_width(src, new_width):
    h, w = src.shape[:2]
    aspect_ratio = h/w
    new_height = new_width / aspect_ratio
    return cv.resize(img, dsize=(int(new_height),new_width), interpolation=cv.INTER_CUBIC)


# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert the path of the image")
args = vars(parser.parse_args())

# Read the image from command line argument
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Invoke the function defined before
zoommed_height = zoom_by_height(img, 507)
zoommed_width = zoom_by_width(img, 507)

# Show the input and output image
cv.imshow("Original", img)
cv.imshow("Zoomed by Height", zoommed_height)
cv.imshow("Zoomed by Width", zoommed_width)
cv.waitKey(0)



############################################ ABOUT INFORMATION ##############################################
#                                                                                                           #
# INTERPOLATION -> The main problem when we zoomed in a picture is the values                               #
#                  of the new pixels added in the zoomed image, for this reason we need to apply            #
#                  a method of interpolation, the best way is CUBIC INTERPOLATION,                          #
#                  try to change INTER_CUBIC with INTER_LINEAR and see how the render is too bad.           #
#                                                                                                           #    
# ASPECT RATIO -> The aspect ratio is most important property, if you don't respect this properties         #
#                 the output image look nasty so we can calculate the new width or the new height           #
#                 based on new width or new height fixed by user.                                           #
#                 ex1. if I fixed the new width, I can calculate the new height with this expression:       #
#                      aspect_ratio = old_width / old_height                                                #
#                      new_height = new_width / aspect_ratio                                                #
#                                                                                                           #
#                 ex2. if I fixed the new height, I can calculate the new width with this expression:       #
#                      aspect_ratio = old_width / old_height                                                #
#                      new_height = new_height * aspect_ratio                                               #
#                                                                                                           #
#############################################################################################################