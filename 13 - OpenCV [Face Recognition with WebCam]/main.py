# OpenCV - Face Recognition with OpenCV
#
# @author Emilio Garzia, 2023

import cv2 as cv
import cv2.data as CVdata   # in this module we can find the XML file with AI model pre-trained

# Load classifier pretrained by openCV
AImodel = cv.CascadeClassifier(CVdata.haarcascades + 'haarcascade_frontalface_default.xml')

# Enable access to the first available imaging device
cam = cv.VideoCapture(0)

while True:
    # Read the frame
    ret, frame = cam.read()
    
    # Convert frame color in grayscale, the face detection work better if the image is in grayscale
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGRA2GRAY)

    # All faces result
    faces_result = AImodel.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5) 

    # If user type "q" on the keyboard the programm will be closed
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
    # Draw a rectangle on the face
    for (x,y,w,h) in faces_result:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    
    # Show the frame
    cv.imshow("Webcam", frame)

# Release all resources after programm ending
cam.release()



######## ABOUT INFORMATION #########
#
# When we invoke detectMultiScale() method in faces_results we can find an n-dimensional array
# every dimension of array contain four important information about every faces detected:
#   ° x coordinate -> The x coordinate of the first pixel of face
#   ° y coordinate -> The y coordinate of the first pixel of face
#   ° w -> width of the face
#   ° h -> height of the face
# 
# We can combine all this four information to draw the rectangle around the face in the frame
#
# detectMultiScale() give in input three arguments:
#   ° input image with our faces to detect
#   ° scaleFactor -> scaling of faces, this parameter is most important to set the sensibility of detection
#                    usually the value of this argument is 1.1
#   ° minNeighbors -> sect how close can be two faces
# 
#################################################################################