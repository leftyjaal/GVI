import cv2 as cv
import os
import sys

from PIL import Image

R720P = (1280, 720)
H720P = (720, 1280)
R1080P = (1920, 1080)


def img_processing(path, hori):
    horientacion = 0

    if hori.upper() == "VERTICAL":
        horientacion = H720P
    else:
        horientacion = R720P
    """
    comprobacion horizontal o vertical
    """
    print("Processing images")
    for item in os.listdir(path):
        if os.path.isfile(path+item):
            # print(path+item)
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize(horientacion, Image.ANTIALIAS)
            imResize.save(f + ".jpg", 'JPEG', quality=90)

    print("Resized")
