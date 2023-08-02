import cv2

video = cv2.VideoCapture('./videos/smile.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
success, frame = video.read()

height = frame.shape[0]
widht = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('blured.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (widht, height))

while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 3)
    for (x, y, w, h) in faces : 
        frame[y:y+h, x: x+w] = cv2.blur(frame[y:y+h, x:x+w],(50,50))
    output.write(frame)
    success, frame = video.read()

output.release()