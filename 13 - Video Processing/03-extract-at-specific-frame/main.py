import cv2

video = cv2.VideoCapture('./videos/video.mp4')
nb_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

timestamp = input('Enter timestamp in hh:mm:ss format : ')

tab_timestamp = timestamp.split(':')
hh, mm, ss = tab_timestamp
tab_timestamp_float = [float(i) for i in tab_timestamp]
hours, minutes, seconds = tab_timestamp_float

frame_nb = hours * 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_nb)
success, frame = video.read()
cv2.imwrite(f'Frame_at_{hh}_{mm}_{ss}.jpeg', frame)