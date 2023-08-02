import os
import cv2;

images = os.listdir('./images')
for image in images:
    gray = cv2.imread(f'images/{image}', 0)
    cv2.imwrite(f'grayimages/gray-{image}', gray)

# color = cv2.imread('./galaxy.jpeg', 0)
# cv2.imwrite('galaxy-gray.jpeg',color)
