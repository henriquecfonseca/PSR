#!/usr/bin/env python3
import cv2

def main():

    # --------------------
    # Initialization
    # -------------------
    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)



    # --------------------
    # Execution
    # -------------------
    _, image = capture.read()  # get an image from the camera



    # --------------------
    # Visualization
    # -------------------

    cv2.imshow('image', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

    # --------------------
    # Termination
    # -------------------
    
if __name__ == '__main__':
    main()