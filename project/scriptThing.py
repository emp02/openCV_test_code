#python 3.8.1
#matplotlib 3.2.2
#numpy 1.18.3
#cv2 4.4.0
#argparse 1.1
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2


#python scriptThing.py --image thatImage.jpeg

#get, load image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image path")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image1 = cv2.imread(args["image"]) #another copy for later use

#colors, for convenience
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)
dpink = (128, 84, 231)

#show original image
cv2.imshow("original", image)
cv2.waitKey(0)

#forehead center calculations, draw circle
foreheadCenter = (image.shape[1]//2 - 12, image.shape[0]//2 - 70)
cv2.circle(image, foreheadCenter, 12, dpink, -1)

#squares in eyes
image[270:275, 260:265] = dpink
image[266:271, 423:428] = dpink

c = 3   #ring size counter
direction = 0   #ring width increasing or decreasing (see below)
#draw rings
for r in range(0, 600, 40):
    color = np.random.randint(150, high=256, size=(3,)).tolist()    #random color
    cv2.circle(image, foreheadCenter, r, color, c)  #draw circle
    #make rings thinner when too large, thicker when too small
    if direction == 0:
        c -= 1
    else:
        c += 1

    #change ring thickness direction (getting larger vs smaller)
    if c == 3:
        direction = 0
    elif c == 1:
        direction = 1

#show image with psychic forehead rings and box eyes
cv2.imshow("circles", image)
cv2.waitKey(0)

#make circular mask centered at forehead
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (foreheadCenter), 350, white, -1)
cv2.imshow("Mask", mask)

#apply mask to image
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("mask on image", masked)
cv2.waitKey(0)

#apply color space + mask to image
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    #color space
masked = cv2.bitwise_and(hsv, hsv, mask=mask)   #mask
cv2.imshow("HSV masked", masked)
cv2.waitKey(0)

#color histograms of face + background(and hands)
chnls = cv2.split(image)
print(chnls)
colors = ("b", "g", "r")
plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("num pixels")

#mask of main face + lower face
#setting up mask
mask1 = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask1, (foreheadCenter[0], foreheadCenter[1]+100), 150, white, -1)   #big face part
cv2.circle(mask1, (foreheadCenter[0], foreheadCenter[1]+200), 105, white, -1)   #small face part
masked1 = cv2.bitwise_and(image, image, mask=mask1)
cv2.imshow("maskhistogram", masked1)    #show masked image

for (chnls, color) in zip(chnls, colors):
    hist = cv2.calcHist([chnls], [0], mask1, [256], [0, 256])   #setting up histogram
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

#blurring
blurred = np.hstack([cv2.GaussianBlur(masked1, (7, 7), 0)])
cv2.imshow("blurred", blurred)
cv2.waitKey(0)

#thresholding time?
greyImage = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
blurred1 = cv2.GaussianBlur(greyImage, (9, 9), 0) #big blur
(T, threshInv) = cv2.threshold(blurred1, 80, 200, cv2.THRESH_BINARY_INV)
#trying different parameters to get the face isolated... not working too well
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.waitKey(0)

#edge detection?
lap = cv2.Laplacian(threshInv, cv2.CV_64F)  #tried the others too... laplacian was the least cluttered
#Not sure how to isolate the face since some shadow parts are the same shade as those not on the face
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

#with regards to the neck part, did threshold thing with new parameters and transplanted neck/chin part onto greyImage, then did contour
#seemed to work ok

greyImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
blurred2 = cv2.GaussianBlur(greyImage, (5, 5), 0)
(T, threshInv1) = cv2.threshold(blurred2, 53, 200, cv2.THRESH_BINARY_INV)
#transplant part of chin/neck that was too similar in color from the threshold thing where I changed the parameters so there was a clear difference
greyImage1[450:500, 400:440] = threshInv1[450:500, 400:440]
cv2.imshow("Grey Image with fixed chin", greyImage1)
cv2.waitKey(0)

#edge detection?
lap1 = cv2.Laplacian(greyImage1, cv2.CV_64F)  #tried the others too... laplacian was the least cluttered
#Not sure how to isolate the face since some shadow parts are the same shade as those not on the face
lap1 = np.uint8(np.absolute(lap1))
cv2.imshow("Laplacian1", lap1)
cv2.waitKey(0)


#cutting/pasting contour
lap2 = cv2.Laplacian(threshInv1, cv2.CV_64F)  #tried the others too... laplacian was the least cluttered
#Not sure how to isolate the face since some shadow parts are the same shade as those not on the face
lap2 = np.uint8(np.absolute(lap2))
lap[450:525, 350:440] = lap2[450:525, 350:440]
cv2.imshow("Laplacian1", lap)
cv2.waitKey(0)
