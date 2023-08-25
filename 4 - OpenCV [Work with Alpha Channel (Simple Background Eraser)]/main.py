# OpenCV - Background Eraser
#
# ℹ: Use the images into "images" directory to try this programm
# ⚠: This program is very simple, so it is not usable in real contexts, but you can use with images with a full white background like the images in the included directory
#
# STEP OF ALGORITHMS:
#   1) Load the image in BGR
#   2) Create a copy of the image with alpha channel (BGRA)
#   3) Find the edges in the image (blur for noise reduction and Canny Algorithm for edge detection)
#   4) Find the contours of the image (use findContours() method) with edges and fill them with white color (use drawContours() method) 
#   5) Now iterate the image with filled contours and when you find a black pixel, set to zero the alpha channel in the image with alpha channel at the same coordinates of image of edges
#   6) Save the image with alpha channel on file system
#
# @author Emilio Garzia, 2023

import cv2 as cv
import argparse as ap

# Init and set parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Insert path of the image")
args = vars(parser.parse_args())

# Read image from command line argument
img = cv.imread(args["image"], cv.IMREAD_UNCHANGED)

# Convert shape of the image in 4 channel image (fourth channel used for Alpha Channel)
img_with_alpha = cv.cvtColor(img, cv.COLOR_BGR2BGRA)

# Calculate height and width of the image
h, w, _ = img_with_alpha.shape

# Segmentation
blurred = cv.GaussianBlur(img, (5,5), 0)
edges = cv.Canny(blurred, 10, 20, apertureSize=3)

# Find the contours
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Fill the color of the shapes in the image
for contour in contours:
    cv.drawContours(edges, [contour], -1, 255, thickness=cv.FILLED)

# If the pixel in the edges is black set to zero the alpha channel of that pixel
for i in range(w):
    for j in range(h):
        if edges[j][i] == 0:
            img_with_alpha[j][i][3] = 0

# Save the new image without background on file system
# ⚠: Save the image with .png extension because only this format include the alpha channel
cv.imwrite("output.png", img_with_alpha)


####### CHANNEL MAP ########
# In a BGRA model the channel map is:
#
# 0 - Channel of BLUE 
# 1 - Channel of GREEN
# 2 - Channel of RED
# 3 - Alpha Channel (transparency)
#
###############################################################