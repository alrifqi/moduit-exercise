import operator
from repository import moduit_repository

async def get_endpoint_one():
    resp = moduit_repository.moduit_get_first_endpoint()
    return resp.json()

async def get_endpoint_two():
    resp = moduit_repository.get_second_endpoint()
    resp = resp.json()
    resp = sorted(_filter_tags_sport(_filter_response_two(resp)), key=lambda k: k['id'], reverse=True)[:3]
    return resp

async def get_endpoint_three():
    resp = moduit_repository.get_three_endpoint()
    resp = resp.json()
    print(resp)
    return resp

def _filter_response_two(resp):
    data = []
    for r in resp:
        if 'title' not in r or 'description' not in r:
            continue
        if 'Ergonomic' in r['title'] or 'Ergonomic' in r['description']:
            data.append(r)
    return data

def _filter_tags_sport(resp):
    data = []
    for r in resp:
        if 'tags' not in r:
            continue

        if 'Sports' in r['tags']:
            data.append(r)
    return data