import cv2
import os

video_path = os.path.expanduser("~/Parking-detection/data/raw/video.mp4")
output = os.path.expanduser("~/Parking-detection/data/frames/")

os.makedirs(output, exist_ok=True)

video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)

interval = int(fps * 0.2)
frame_idx = 0
saved = 0

while True:
    ret, frame = video.read()
    if not ret:
        break
    if frame_idx % interval == 0:
        cv2.imwrite(os.path.join(output, f"Frame_{saved:04d}.jpg"), frame, [cv2.IMWRITE_JPEG_QUALITY, 95]) 
        saved += 1
    frame_idx += 1

video.release()
print(f"Saved: {saved} frames")







