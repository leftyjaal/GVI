import cv2 as cv
import os
import sys

from PIL import Image

R720P = (1280, 720)
R1080P = (1920, 1080)


def img_processing(path):
    """
    comprobacion horizontal o vertical
    """
    print("Processing images")
    for item in os.listdir(path):
        if os.path.isfile(path+item):
            # print(path+item)
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize(R720P, Image.ANTIALIAS)
            imResize.save(f + ".jpg", 'JPEG', quality=90)

    print("Resized")
