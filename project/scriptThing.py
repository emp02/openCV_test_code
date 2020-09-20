import numpy as np
import argparse
import cv2

#python scriptThing.py --image ../../images/thatImage.jpeg

#get, load image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image path")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

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
