import boto3
from boto3.session import Session
import os

IMG_BUCKET = 'gvi-images'
VID_BUCKET = 'gvi-videos'


def upload():
    print("uploading")
