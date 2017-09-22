import os
import requests
import json


def get_operations_name(file_name, bitrate):
    speech_api = os.environ['GOOGLE_SPEECH_API_KEY']
    url = "https://speech.googleapis.com/v1/speech:longrunningrecognize?key=" + speech_api
    data = {
        "config": {
            "encoding": "FLAC",
            "sampleRateHertz": bitrate,
            "languageCode": "ko-KR",
        },
        "audio": {
            "uri": "gs://speech-suwon/" + file_name + ".flac"
        }
    }
    response = requests.post(url, data=json.dumps(data))
    content = response.json()
    operations_name = content.get('name')
    print(operations_name)
    return operations_name
