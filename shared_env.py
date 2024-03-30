import configparser
import os 
config = configparser.ConfigParser()
config.read(os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'config.ini')))
HOST_ENV = config['ENV']
