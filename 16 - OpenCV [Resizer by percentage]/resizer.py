# Image Resizer
# @author Emilio Garzia, 2024

import cv2 as cv
import argparse as ap
import os

# Resize the image by the percentage
def resize_image(img, percentage=50):
    percentage = float(percentage) 
    width = int(img.shape[1] * (percentage / 100))
    height = int(img.shape[0] * (percentage / 100))
    return cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)

# Parser
parser = ap.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Specify the input image")
parser.add_argument("-p", "--percentage", required=True, help="Specify the percentage of the resize")
parser.add_argument("-s", "--show", action="store_true", help="Show the result of the resize operation")
parser.add_argument("-n", "--no_save", action="store_true", help="Don't save the output image")
parser.add_argument("-o", "--overwrite", action="store_true", help="Overwrite the original image with the output image")
parser.add_argument("-e", "--extension", default=".png" ,help="Specify extension for the output image")
args = vars(parser.parse_args())

# Driver code
if __name__ == "__main__":
    img = cv.imread(args["image"], cv.IMREAD_ANYCOLOR)
    resized = resize_image(img, args["percentage"])

    if not args["no_save"]:
        filename = str(args["image"]).split(".")[-2]
        
        if args["overwrite"]:
            os.remove(args["image"])
            filename = filename+args["extension"]
            cv.imwrite(filename=filename, img=resized)
        else:
            filename = filename+"_resized"+args["extension"]
            cv.imwrite(filename=filename, img=resized)

    if args["show"]:
        cv.imshow("Original", img)
        cv.imshow("Resized", resized)
        cv.waitKey(0)