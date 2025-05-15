import cv2
import os

video_path = 'video.mp4'

output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

interval = 0.1

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error ao abrir o vídeo.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps * interval)  

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f'frame_{saved_count:05d}.jpg')
        cv2.imwrite(filename, frame)
        print(f'Save: {filename}')
        saved_count += 1

    frame_count += 1

cap.release()
print("Done.")
