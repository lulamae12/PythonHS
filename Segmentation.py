#!/usr/bin/env python
import numpy as np
import cv2

## WRITE YOUR CODE HERE

img = cv2.imread('BigSquares.png') #Located in MIT folder
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
