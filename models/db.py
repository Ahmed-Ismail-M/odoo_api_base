import requests
from shared_env import HOST_ENV
url = HOST_ENV['url']
class DBManager:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.session = requests.Session()


    def create_db(self):
        params = { 'name': self.db_name,
        'password': HOST_ENV['password'],
        'master_pwd':HOST_ENV['master_pwd'],
        'lang':'en_US',
        'phone':"","login":HOST_ENV['login']
    }
        
        response = self.session.post(f'{url}/web/database/create', data=params, allow_redirects=False)
        return response


    