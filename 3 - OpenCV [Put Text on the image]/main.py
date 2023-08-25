# OpenCV - How to put text on the image with OpenCV
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i","--image", required=True, help="Insert path of the image")
args = vars(parser.parse_args())

# Read the image from command line argument
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Set the text to put on image and set all properties of text
my_text = "Hello World!"
font = cv.FONT_HERSHEY_DUPLEX
position = (50,100)
font_scale = 1
font_color = (0,0,0)
thickness = 1

# Put the text on the image
cv.putText(img, my_text, position, font, font_scale, font_color, thickness=thickness)

# Show the image with text
cv.imshow("My image with text", img)
cv.waitKey(0)

##### Centered text ######

# Use this function to get the right coordinates for centered text
def getCoordinatesForCenteredText(image, text, font, font_scale, thickness):
    text_size = cv.getTextSize(text, font, font_scale, thickness)[0]
    img_height, img_width, _ = image.shape
    x = (img_width - text_size[0]) // 2
    y = (img_height + text_size[1]) // 2

    return x,y

x, y = getCoordinatesForCenteredText(img, my_text, font, font_scale, thickness)
cv.putText(img, my_text, (x,y), font, font_scale, thickness)
cv.imshow("Image with centered text", img)
cv.waitKey(0)
