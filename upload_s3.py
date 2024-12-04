import os

import boto3


def upload_to_s3(file_path, bucket, key):
    files = os.listdir("tmp")
    print("Files in /tmp directory:", files)
    print("UPLOADING")
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket, key)
    print("UPLOAD DONE")
