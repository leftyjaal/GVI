import cv2 as cv
from moviepy.editor import *

from PIL import *


def render(obj, folder, music):
    musica = ""
    img_index = []
    video_len = 0

    if music.upper() == "FELIZ":
        musica = "feliz.mp4"
    if music.upper() == "DIA ESPECIAL":
        musica = "especial.wav"
    if music.upper() == "POP REMIX":
        musica = "pop.wav"
    else:
        musica = "instrumental.mp4"

    for item in obj:
        img_index.append(item.path)

    # img_index.append("src/drawing.jpg")
    # img_index.append("src/drawing.jpg")

    clip = ImageSequenceClip(img_index, fps=1)

    clip.write_videofile(f"requests/{folder}/{folder}.mp4")

    videoclip = VideoFileClip(f"requests/{folder}/{folder}.mp4")
    video_len = videoclip.duration

    print(f"video len: {video_len}")

    audioclip = AudioFileClip(f"src/{musica}")
    # audioclip = AudioFileClip(f"src/musica.wav")
    clipaudio = audioclip.subclip(0, video_len)

    new_audioclip = CompositeAudioClip([clipaudio])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f"requests/{folder}/{folder}.mp4")
