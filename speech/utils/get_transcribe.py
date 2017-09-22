import requests
import json

from .download_blob import download_blob
from .upload_blob import upload_blob
from .mp3_to_flac import mp3_to_flac
from .get_operations_name import get_operations_name


def call_transcribe_request(file_name):
    # 1. download
    mp3_full_name = file_name + ".mp3"
    download_blob(mp3_full_name)
    print("Download done")

    # 2. convert
    bitrate = mp3_to_flac(file_name)
    print("Converting to flac done")

    # 3. upload
    # upload시 data를 public하게 만들어줘야 아래에서 operation 할 수 있음
    flac_full_name = file_name + ".flac"
    upload_blob(flac_full_name)
    print("Upload done")

    # 4. get operation name
    operations_name = get_operations_name(file_name, bitrate)
    print("Operation_name is '{i}'".format(i=operations_name))
    return operations_name
