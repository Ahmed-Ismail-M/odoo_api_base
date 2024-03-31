import requests
from shared_env import HOST_ENV
import json
url = HOST_ENV['url']
class DBManager:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.session = requests.Session()
        self.session_id = ""


    
    def create_db(self):
        params = { 'name': self.db_name,
        'password': HOST_ENV['password'],
        'master_pwd':HOST_ENV['master_pwd'],
        'lang':'en_US',
        'phone':"","login":HOST_ENV['login']
    }
        
        response = self.session.post(f'{url}/web/database/create', data=params, allow_redirects=False)
        return response
    
    def login(self)-> str:
        data = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'db': self.db_name,
                'login': HOST_ENV['login'],
                'password': HOST_ENV['password'],
            },
        }
        response = requests.post(f'{url}/web/session/authenticate', json=data)

        if response.status_code == 200:
            return response.cookies.get('session_id')
        else:
            raise Exception(response.content)
        
    def create_model(self, model_name:str, fields:list):
        headers = {
    'Content-Type': 'application/json',
    'X-Openerp-Session-Id': self.login(),
}
        model_data = {
    'name': f'x_{model_name}',
    'model': f'x_{model_name}',
    'field_id':fields
}
        create_table_data = {
    'jsonrpc': '2.0',
    'method': 'execute_kw',
    'params': {
        'model': 'ir.model',
        'method': 'create',
        'args': [model_data
        ],
        'kwargs': {
            'context': {
                'lang': 'en_US',
                'tz': 'UTC',
            },
        },
    },
}
        response = requests.post(f'{url}/web/dataset/call_kw', headers=headers, data=json.dumps(create_table_data))



    