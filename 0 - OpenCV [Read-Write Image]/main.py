# OpenCV - Read/Write the image
#
# @author Emilio Garzia, 2023  

import cv2
import argparse as ap

#Init and set arguments parser
arguments = ap.ArgumentParser()
arguments.add_argument("-i", "--image", required=True, help="Image path")
args = vars(arguments.parse_args())

#Read the image from command line arguments
img = cv2.imread(args["image"], cv2.IMREAD_COLOR)

#Some information about the image
print("Number of channel: {0}".format(img.shape))
print("Data type of the image: {0}".format(img.dtype))

#Height and Width of my image
height = img.shape[0]
width = img.shape[1]
print("Height of image: {0}".format(height))
print("Width of image: {0}".format(width))

#Show the image
cv2.imshow("Output of my image", img)
cv2.waitKey(0)

#Draw a diagonal line on the image and show them
p1 = (0,0)
p2 = (height-1, width-1)
cv2.line(img=img, pt1=p1, pt2=p2, color=(0,0,255), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("Output with diagonal", img)
cv2.waitKey(0)

#Save a copy of the image with diagonal on File System
cv2.imwrite("myImageWithDiagonal.png", img)