import tensorflow as tf
import tensorflow.keras
import numpy as np
import boto3
import cv2
import moviepy
import PIL

from downloader import download
from classifier import classifier_main
from img_processor import img_processing
from img_renderer import render
from uploader import upload

print(f"Tensorflow: {tf.__version__}")
print(f"Keras:      {tensorflow.keras.__version__}")
print(f"Numpy:      {np.__version__}")
print(f"AWS SDK:    {boto3.__version__}")
print(f"OpenCV:     {cv2.__version__}")
print(f"Pillow:     {PIL.__version__}")
print(f"Moviepy:    {moviepy.__version__}")


if __name__ == '__main__':
    S3_folder = "1234"

    print("DOWNLOAD FUNCTION")
    img_dir_list = download(S3_folder)
    print("IMG FUNCTION")
    img_processing(f"requests/{S3_folder}/")
    print("CLASS FUNCTION")
    class_list = classifier_main(f"requests/{S3_folder}/")
    print("RENDER FUNCTION")
    render(class_list, S3_folder)
    print("UPLOAD FUNCTION")
    upload(S3_folder)

    print("main finish")
