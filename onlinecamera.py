# import the necessary packages
import numpy as np
import argparse
import imutils
import time
import cv2
import os
from imutils.video import VideoStream
from imutils.video import FPS
import matplotlib.pyplot as plt

vcap = cv2.VideoCapture('http://192.168.0.6:8000/stream.mjpg')
while(True):
    # Capture frame-by-frame
    ret,frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        #cv2.imshow('Frame',frame)
        plt.imshow(frame)
        plt.show()

        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print ("Video stop")
