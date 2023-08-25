# OpenCV [HighGUI] - Mouse Event (Click and Drag)
#
# @details Click on the pixels of the image and see the coordinates in the terminal output
# @author Emilio Garzia, 2023

import cv2 as cv
import numpy as np

# Define the function that manage the Mouse Event
def my_mouse_event(event, x, y, flags, param):
    global img

    # print the pixel coords when user click the left button or dragged on the image
    if event == cv.EVENT_LBUTTONDOWN or (flags & cv.EVENT_FLAG_LBUTTON):
        print("Coords: ({},{})".format(x,y))

# Create a new total black image
img = np.ones((500, 500, 3), np.uint8)

# Show the black image
cv.imshow("Image", img)

# Associate the function to Mouse Callback Event
cv.setMouseCallback("Image", my_mouse_event)

# Run the programm until the user don't type "q" on the keyboard
while True:
    key = cv.waitKey(1)

    if key == ord("q"):
        break

cv.destroyAllWindows()