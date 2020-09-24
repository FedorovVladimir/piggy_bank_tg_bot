import requests

BASE_URL = 'http://localhost:8080'
HEADERS = {'content-type': 'application/json;charset=UTF-8'}


def get(path: str):
    return requests.get(BASE_URL + path, headers=HEADERS)


def post(path: str, body: str):
    return requests.post(BASE_URL + path, body.encode('UTF-8'), headers=HEADERS)
