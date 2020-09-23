# openCV_test_code

TECHNICALLY DONE, I guess. I suggest you look at the image first. 

Chapter 3: load, display image
Chapter 4: set pixels in eyes to different color
Chapter 5: drew circles in random colors centered on forehead, alternating line width
Chapter 6: masking, circular mask on face w/ color space and previous circles... tried to isolate face with mask by making mask with multiple circles :\
Chapter 7: did a histogram of the section of the face that I got with mask from previous section. Wanted to try histogram with a more complete face and compare to background, but...
Chapter 8: Tried different blurs to see what would help best with the thresholding later on (ended up just going with Gaussian, not sure if my testing are in previous commits, I don't think so)
Chapter 9, 10: Thresholding + trying to make contour of face. I tried a lot of the different functions & parameters, but never got anything that really helped. The one I ended up with was the best (others were too messy)

In the end I just committed what I ended up with because the project is due, but I was in the middle of trying to find combinations of blur/threshold/contour to get a good capture of the face... I think the issue is that the values of parts of the face (bottom-right chin) were too similar to adjacent parts(neck), and I couldn't figure out how to get around this easily (tried different color spaces to see if they would help, but.) Easiest way would probably be just drawing a line around those sections? 
