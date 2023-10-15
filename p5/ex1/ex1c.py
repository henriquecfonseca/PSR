#!/usr/bin/env python3

import cv2
import argparse

def main():
    parser = argparse.ArgumentParser(description='Display an image')
    parser.add_argument('image_path_1')
    args = parser.parse_args()

    image_2= cv2.imread(args.image_path_2, cv2.IMREAD_COLOR)  # Load the specified image


    cv2.imshow('Image', image_2)  # Display the image
    cv2.waitKey(0)  # Wait for a key press before proceeding


if __name__ == '__main__':
    main()
