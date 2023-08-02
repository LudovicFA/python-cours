import os
import cv2;

INPUT_FOLDER = './images'
OUTPUT_FOLDER = './faces'

CASCADE = 'faces.xml'
SCALE = 1.1
NEIGHBORS = 4
COLOR = (255, 255, 0)
WIDTH = 4

def has_face(image_path):
    image = cv2.imread(image_path, 1)
    face_cascade = cv2.CascadeClassifier(CASCADE)
    faces = face_cascade.detectMultiScale(image, SCALE, NEIGHBORS)
    if len(faces) != 0 :
        for (x, y, w, h) in faces : 
            cv2.rectangle(image,(x, y), (x + w, y + h), COLOR, WIDTH)
        return image


images = os.listdir(INPUT_FOLDER)
for image in images:
    face_image = has_face(f'{INPUT_FOLDER}/{image}')
    if face_image is not None:
        cv2.imwrite(f'{OUTPUT_FOLDER}/{image}', face_image)
