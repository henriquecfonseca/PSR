#!/usr/bin/env python3 
import argparse
import cv2
from functools import partial

def onTrackbar(image_gray, val, *args):
    
    _,thresh = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow('window - Ex3a', thresh)

def main():
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-im', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)

    cv2.namedWindow('window - Ex3a')
    cv2.imshow('Original',image)
    onTrackbar(image_gray, 100, 'window - Ex3a')

    cv2.createTrackbar('Threshold','window - Ex3a', 0, 255, partial(onTrackbar,image_gray))

    cv2.waitKey(0)

if __name__ == '__main__':
    main()