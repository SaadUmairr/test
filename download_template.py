import os

import boto3


def download_from_s3(bucket, key, download_path):
    print("DOWNLOADING FILE")
    s3 = boto3.client("s3")
    # s3.download_file(bucket, key, download_path)
    s3.download_file(
        "surmountpublicschool", "homework/01-12-24/01-12-2024.docx", "/tmp/output.docx"
    )
    print("DOWNLOADED at ", download_path)
    files = os.listdir("/tmp")
    print("AFTER DOWNLOAD: Files in /tmp directory:", files)


