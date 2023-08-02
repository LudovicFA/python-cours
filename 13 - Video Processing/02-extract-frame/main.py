import cv2

video = cv2.VideoCapture('./videos/video.mp4')
success, frame = video.read()

count = 1
while success:
    cv2.imwrite(f'./images/{count}.jpeg', frame)
    success, frame = video.read()
    count += 1