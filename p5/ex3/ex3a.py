#!/usr/bin/env python3 
import argparse
import cv2

# Global variables
val = 200
image_gray = None
window_name = 'window - Ex3a'



def onTrackbar(threshold):
    
    _,thresh = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, thresh)

def main():
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-im', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
        
    cv2.imshow('Original',image)

    global image_gray # use global var

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)

    cv2.namedWindow(window_name)
    
    cv2.createTrackbar('Threshold' % val, window_name, 0, 255, onTrackbar)

    onTrackbar(val)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()