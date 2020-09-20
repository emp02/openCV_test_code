import numpy as np
import argparse
import cv2

ap = argpase.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the object")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[30:120, 240:335]
cv2.imshow("T-Rex Face", image)
