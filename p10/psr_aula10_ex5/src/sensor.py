#!/usr/bin/env python3
import cv2
from cv_bridge import CvBridge


def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    bridge = CvBridge()
    while True:
        _, image = capture.read()  # get an image from the camera

        image_message = bridge.cv2_to_imgmsg(image, encoding="passthrough")
        
        # add code to show acquired image
        cv2.imshow(window_name,image_message)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        # add code to wait for a key press
    capture.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()