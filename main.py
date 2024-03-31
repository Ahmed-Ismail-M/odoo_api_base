from models.db import DBManager
from shared_env import HOST_ENV
models = [{'model_name': 'emps', 'fields': [(0,0,{'name':'x_test_name','ttype': 'char',
                'required': False,}),
                (0,0,{'name':'x_empid','ttype': 'char',
                'required': True,'index':True})]
           }]
for model in models:

    print(DBManager(HOST_ENV['new_db']).create_model(model['model_name'], model['fields']))
