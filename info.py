import tensorflow as tf
import tensorflow.keras
import numpy as np
import boto3
import cv2
import moviepy
import PIL


if __name__ == '__main__':
    print(f"Tensorflow: {tf.__version__}")
    print(f"Keras:      {tensorflow.keras.__version__}")
    print(f"Numpy:      {np.__version__}")
    print(f"AWS SDK:    {boto3.__version__}")
    print(f"OpenCV:     {cv2.__version__}")
    print(f"Pillow:     {PIL.__version__}")
    print(f"Moviepy:    {moviepy.__version__}")
