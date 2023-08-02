import cv2
import os
import numpy

# Original images must have same dimension => to improve

COLUMNS = 3
ROWS = 2
IMAGES_DIRECTORY = './images'

HORIZONTAL_MARGIN = 40
VERTICAL_MARGIN = 20

images = os.listdir(IMAGES_DIRECTORY)
image_objects = [cv2.imread(f'{IMAGES_DIRECTORY}/{filename}') for filename in images]
SHAPE = cv2.imread(f'{IMAGES_DIRECTORY}/1.jpeg').shape

big_image = numpy.zeros((SHAPE[0] * ROWS + HORIZONTAL_MARGIN * (ROWS + 1), 
                        SHAPE[1] * COLUMNS + VERTICAL_MARGIN * (COLUMNS + 1),
                        SHAPE[2]), numpy.uint8)
big_image.fill(255)

positions = [(x,y) for x in range(COLUMNS) for y in range(ROWS)]
print(positions)
for (pos_x, pos_y), image in zip(positions, image_objects):
    x = pos_x * (SHAPE[1] + VERTICAL_MARGIN) + VERTICAL_MARGIN
    y = pos_y * (SHAPE[0] + HORIZONTAL_MARGIN) + HORIZONTAL_MARGIN
    big_image[y:y+SHAPE[0], x:x+SHAPE[1]] = image


cv2.imwrite('grid.jpeg',big_image)
