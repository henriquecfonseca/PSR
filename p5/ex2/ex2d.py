#!/usr/bin/env python3 
import cv2
import numpy as np

def main():

    image_filename = '../images/atlas2000_e_atlasmv.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image'
    threshold_level_b = 50
    threshold_level_g = 100
    threshold_level_r = 150


    lower_bound = np.array([0,50,0])
    upper_bound = np.array([50,256,50])

    #masking the image using inRange() function
    image_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)


    # Resoult of comaundigng
    cv2.imshow('Mask Image', image_mask)
    cv2.imshow('Tresh RGB', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()