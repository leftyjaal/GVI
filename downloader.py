import boto3
from boto3.session import Session
import os

IMG_BUCKET = 'gvi-images'
VID_BUCKET = 'gvi-videos'


def download(folder):
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(IMG_BUCKET)
    serial = 0
    img_dir_list = []

    # if not os.path.exists(f"renderer/requests/{folder}"):
    if not os.path.exists(f"requests/{folder}"):
        print("Directory created")
        os.mkdir(f"requests/{folder}")
        # os.mkdir(f"renderer/requests/{folder}")

    else:
        print("Directory already exists")

    print("Downloading files...")
    for my_bucket_object in my_bucket.objects.filter(Prefix=f"{folder}/"):

        if my_bucket_object.key != f"{folder}/":
            serial = serial + 1

            my_bucket.download_file(my_bucket_object.key, f"requests/{folder}/{serial}.jpg")
            # my_bucket.download_file(my_bucket_object.key, f"renderer/requests/{folder}/{serial}.jpg")

            img_dir_list.append(f"requests/{folder}/{serial}.jpg")
            # img_dir_list.append(f"renderer/requests/{folder}/{serial}.jpg")

    print(f"Finished. Files downloaded at request/{folder}")
    return img_dir_list
