# OpenCV - Slider widget for contrast and brightness management
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Global value
alpha = 100
beta = 0

# Function to associate at slider event for brightness
def brightness_changed(value):
    global beta, img, alpha
    beta = value
    new_image = img.copy()
    new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
    cv.imshow("Image", new_image)

# Function to associate at slider event for contrast
def contrast_changed(value):
    global beta, img, alpha
    alpha = value/100
    new_image = img.copy()
    new_image = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
    cv.imshow("Image", new_image)
    
# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert path of the image")
args = vars(parser.parse_args())

# Read the image (default encoding is BGR if you use IMREAD_COLOR)
img = cv.imread(args["image"], cv.IMREAD_COLOR)

# Set the name window to associate the slider
cv.namedWindow("Image")

# Add brightness slider to window
cv.createTrackbar("Brightness", "Image", beta, 300, brightness_changed)

# Add contrast slider to window
cv.createTrackbar("Contrast", "Image", int(alpha), 100, contrast_changed)

# Run the programm until user don't type "q" on the keyboard
while True:
    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindows()


############################################ PROTOTYPE OF createTrackbar() ##############################################
#                                                                                                                       #
#   createTrackbar(nameOfSlider: String, nameOfWindowToAssociateSlider: String, startValue: integer, maxValue: Integer) #
#                                                                                                                       #
#########################################################################################################################