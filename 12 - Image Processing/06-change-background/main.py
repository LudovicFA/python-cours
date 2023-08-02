import cv2
import numpy as np

foreground =  cv2.imread('./images/giraffe.jpeg')
background =  cv2.imread('./images/safari.jpeg')

width = foreground.shape[1]
height = foreground.shape[0]

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j,i]
        if np.any(pixel == [0,255, 0]) :
            foreground[j,i] = resized_background[j,i]

cv2.imwrite('out.jpeg', foreground)