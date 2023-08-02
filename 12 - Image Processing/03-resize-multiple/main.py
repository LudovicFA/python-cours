import os
import cv2;

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)


def resize(image_path, scale_precentage, resize_path):
    image = cv2.imread(image_path) 
    new_dim = calculate_size(scale_precentage, image.shape[1], image.shape[0]) 
    resize_image = cv2.resize(image,new_dim)
    cv2.imwrite(resize_path, resize_image)


images = os.listdir('./images')
for image in images:
    resize(f'images/{image}', 10,f'resized/{image}' )
