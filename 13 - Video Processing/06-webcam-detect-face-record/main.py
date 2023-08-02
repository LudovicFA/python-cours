import cv2

video = cv2.VideoCapture(0)
fps = video.get(cv2.CAP_PROP_FPS)
success, frame = video.read()

height = frame.shape[0]
widht = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (widht, height))

while success:
    faces = face_cascade.detectMultiScale(frame, 1.2, 8)
    for (x, y, w, h) in faces : 
        cv2.rectangle(frame,(x, y), (x + w, y + h), (255, 255, 255), 4)
    cv2.imshow("Recording...", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    output.write(frame)
    success, frame = video.read()

output.release()
video.release()
cv2.destroyAllWindows()