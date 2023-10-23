#!/usr/bin/env python3

import argparse
import cv2


def main():

    # --------------------
    # Initialization
    # -------------------
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary

    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    h, w, nc =image_rgb.shape
    

    # --------------------
    # Execution
    # -------------------
    
    #Draw a circle on image
    xc = int(w/2)
    yc = int(h/2)
    cv2.circle(image_rgb, (xc,yc), 55, (255,0,0), -1) 


    # --------------------
    # Visualization
    # -------------------

    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()