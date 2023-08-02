import cv2

cat = cv2.imread('cat.jpg')

video = cv2.VideoCapture('./videos/smile.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
success, frame = video.read()

height = frame.shape[0]
widht = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('cat.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (widht, height))

while success:
    faces = face_cascade.detectMultiScale(frame, 1.3, 6)
    for (x, y, w, h) in faces : 
        cat_resize = cv2.resize(cat, (w, h))
        place = frame[y:y+h, x:x+w]
        cv2.imwrite('./tmp/cat_resize.jpg', place)
        blend = cv2.addWeighted(place, 0, cat_resize, 1,0)
        cv2.imwrite('./tmp/fcat.jpg', blend)
        frame[y:y+h, x:x+w] = blend
    output.write(frame)
    success, frame = video.read()

output.release()
