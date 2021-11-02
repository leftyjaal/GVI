import cv2 as cv
from moviepy.editor import *

from PIL import *


def render(obj, folder):
    img_index = []

    for item in obj:
        img_index.append(item.path)

    # img_index.append("src/")

    clip = ImageSequenceClip(img_index, fps=1)
    clip.write_videofile(f"requests/{folder}/{folder}.mp4")
