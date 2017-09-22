import os
import requests
import json


def get_result(operation_name):
    speech_api_key = os.environ['GOOGLE_SPEECH_API_KEY']
    url = "https://speech.googleapis.com/v1/operations/{name}?key={key}".format(name=operation_name, key=speech_api_key)
    response = requests.get(url)
    content = response.json()
    try:
        progress = content.get('metadata').get('progressPercent')
        if progress == 100:
            alternatives = content.get('response').get('results')
            result = ''
            for alternative in alternatives:
                result += alternative.get('alternatives')[0].get('transcript')
                result += '\n'
            print(result)
            return result
        else:
            doing = progress
    except:
        doing = 0
        print(doing)
        return doing
