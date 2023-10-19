#!/usr/bin/env python3 
import cv2
import numpy as np

def main():


    image_filename = '../images/atlas2000_e_atlasmv.png'
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image'


    lower_bound = np.array([30,150,80])
    upper_bound = np.array([70,255,255])
    #masking the image using inRange() function
    # image_mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
    image_hsv_mask = cv2.inRange(image_hsv,lower_bound, upper_bound)


    # Resoult of comaundigng
    #cv2.imshow('Mask Image', image_mask)
    cv2.imshow('Mask Image', image_hsv_mask)
    cv2.imshow('Tresh RGB', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding



if __name__ == '__main__':
    main()