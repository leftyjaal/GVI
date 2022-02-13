import boto3
from boto3.session import Session
import os

IMG_BUCKET = 'NAME'
VID_BUCKET = 'NAME'


def upload(folder):
    print("uploading")
    s3 = boto3.resource('s3')
    s3.Bucket(VID_BUCKET).upload_file(f"requests/{folder}/{folder}.mp4", f"{folder}/{folder}.mp4")
    print("uploaded")
