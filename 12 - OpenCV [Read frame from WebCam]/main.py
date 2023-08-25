# OpenCV - Read frame from video source
#
# @author Emilio Garzia, 2023

import cv2 as cv

# Get the first available cam on your pc
cam = cv.VideoCapture(0)

while True:
    # Read the frame
    ret, frame = cam.read()

    # Show the frame
    cv.imshow("Cam", frame)

    # The programm runs until the user types "q" on the keyboard
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Release the resource (the webcam)
cam.release()


##################################################### ABOUT INFORMATION #############################################################
#                                                                                                                                   
# ⚠: The VideoCapture(0) method allows us to instantiate an object that represents our imaging device.                             
#     The whole that we pass in input indicates to which device we want to connect, if there are more cameras connected to the pc, 
#     in our case we have inserted 0 which indicates to connect to the primary camera (the first available)
#
# ⚠: The ord() function is a built-in python function written in C that returns the UNICODE encoding of the input character
#
# ⚠: In the comparison that establishes the closure of the program, is simply expected an input every millisecond "waitKey(1)",
#     After that, if the ASCII returned from waitKey() is equal to the last 8bit (with 0xff mask) of the ASCII value we specified ord("q")
#
# ⚠: The cam object read() function returns two outputs                                                                                                       
#       ° ret = a boolean value that is true if the frame from the camera has been taken correctly                       
#       °frame = the actual frame that can be safely displayed with the imshow() method         
#
#####################################################################################################################################