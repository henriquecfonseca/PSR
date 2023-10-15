#!/usr/bin/env python3

import cv2
import argparse

def main():
    parser = argparse.ArgumentParser(description='Display an image')
    parser.add_argument('image_path')
    args = parser.parse_args()

    image = cv2.imread(args.image_path, cv2.IMREAD_COLOR)  # Load the specified image

    
    cv2.imshow('Image', image)  # Display the image
    cv2.waitKey(0)  # Wait for a key press before proceeding


if __name__ == '__main__':
    main()
