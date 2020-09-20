import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "-image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

print("max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: " + str(cv2.subtract(np.uint8[50]), np.uint8([100])))

print("wrap around: " + str(np.uint8([200]) + np.uint8([100])))
print("wrap around: " + str(np.uint8([50]) - np.uint([100])))

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtraced", subtracted)
cv2.waitKey(0)