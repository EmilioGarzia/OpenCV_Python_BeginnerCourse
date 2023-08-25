#_________________________________________________________________
# In this module you can find the most used
# filter for 2D convolution in image processing.
# 
# @author Emilio Garzia, 2023
#_________________________________________________________________

import numpy as np

# strong property is used to determinate the strongbility of the blurring effect
def mean_blurring(strong:int = 1):
    return np.ones((3,3))/strong

def prewitt_vertical():
    return np.array([[-1,0,1],
                     [-1,0,1],
                     [-1,0,1]])

def prewitt_horizontal():
    return np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])

def laplacian_edge():
    return np.array([[0,1,0],
                     [1,-4,1],
                     [0,1,0]])

def laplacian_blur():
    return np.array([[1,1,1],
                     [1,-8,1],
                     [1,1,1]])

def sharpening():
    return np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]])

def sobel_horizontal():
    return np.array([[-1,-2,-1],
                     [0,0,0],
                     [1,2,1]])

def sobel_vertical():
    return np.array([[-1,0,1],
                     [-2,0,2],
                     [-1,0,1]])

def roberts_gx():
    return np.array([[-1,0],
                     [0,1]])

def roberts_gy():
    return np.array([[0,-1],
                     [1,0]])

def prewitt_gx():
    return np.array([[0,1,1],
                     [-1,0,1],
                     [-1,-1,0]])

def prewitt_gy():
    return np.array([[-1,-1,0],
                     [-1,0,1],
                     [0,1,1]])

def sobel_gx():
    return np.array([[0,1,2],
                     [-1,0,1],
                     [-2,-1,0]])

def sobel_gy():
    return np.array([[-2,-1,0],
                     [-1,0,1],
                     [0,1,2]])

def LoG():
    return np.array([[0,0,-1,0,0],
                     [0,-1,-2,-1,0],
                     [-1,-2,16,-2,-1],
                     [0,-1,-2,-1,0],
                     [0,0,-1,0,0]])