import os
import subprocess
from io import BytesIO

import boto3

# Custom functions
from convert_pdf import convert_word_to_pdf
from download_template import download_from_s3
from upload_s3 import upload_to_s3


def lambda_handler():
    bucket = "surmountpublicschool"
    key = "homework/01-12-24.docx"

    download_path = "/tmp/output.docx"
    tmp_path = "/tmp"

    download_from_s3(bucket, key, download_path)

    soffice_path = "/instdir/program/soffice.bin"

    is_converted = convert_word_to_pdf(soffice_path, "/tmp/output.docx", "/tmp/")

    if is_converted:
        upload_to_s3("/tmp/output.pdf", "surmountpublicschool", "homework/04-12-24.pdf")
        return {"statusCode": 200, "response": "UPLOAD HO GYI FINALLY"}

    return {"statusCode": 400, "response": "ERROR UPLOADING FILE"}