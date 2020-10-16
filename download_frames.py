import pafy
import cv2
import os
import argparse
from slugify import slugify

parser = argparse.ArgumentParser("download_frames.py")
parser.add_argument("video_url", help="Youtube video URL", type=str)
args = parser.parse_args()

pafy_new = pafy.new(args.video_url)
best_video = pafy_new.getbest()

slug_name = slugify(best_video.title)
capture = cv2.VideoCapture(best_video.url)
total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

save_image_every = 0
frame_count = 0

if not os.path.exists(f'results/{slug_name}'):
    os.makedirs(f'results/{slug_name}')

print("Downloading every 10 frames from video")

while True:
    ret, frame = capture.read()

    if not ret:
        print("DONE!")
        break

    frame_count += 1

    if save_image_every == 15:
        path = f'./results/{slug_name}/{str(frame_count)}.jpg'
        cv2.imwrite(path, frame)

        print("Saved to: " + path)
        save_image_every = 0
    else:
        save_image_every += 1

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()