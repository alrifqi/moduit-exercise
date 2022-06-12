import requests
from config.config import settings

ENDPOINT_FIRST = '/backend/question/one'
ENDPOINT_SECOND = '/backend/question/two'
ENDPOINT_THREE = '/backend/question/three'
HEADERS = {
    'User-Agent': 'ModuitConsumer'
}

def get_first_endpoint():
    url = f'{settings.MODUIT_ENDPOINT}{ENDPOINT_FIRST}'
    return requests.get(url, headers=HEADERS)

def get_second_endpoint():
    url = f'{settings.MODUIT_ENDPOINT}{ENDPOINT_SECOND}'
    return requests.get(url, headers=HEADERS)

def get_three_endpoint():
    url = f'{settings.MODUIT_ENDPOINT}{ENDPOINT_THREE}'
    return requests.get(url, headers=HEADERS)
