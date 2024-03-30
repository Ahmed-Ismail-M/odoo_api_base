import requests
from shared_env import HOST_ENV
import json
url = HOST_ENV['url']

def login(db, user, password):
    data = {
        'jsonrpc': '2.0',
        'method': 'call',
        'params': {
            'db': db,
            'login': user,
            'password': password,
        },
    }
    response = requests.post(f'{url}/web/session/authenticate', json=data)

    if response.status_code == 200:
        session_id = response.cookies.get('session_id')

    else:
        raise Exception(response.content)
    return session_id