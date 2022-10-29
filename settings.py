import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get('BOT_TOKEN')


ip = os.environ.get('ip')
PG_USER = os.environ.get('PG_USER')
PG_PASSWORD = os.environ.get('PG_PASSWORD')
DATABASE = os.environ.get('DATA_BASE')

PG_URI = f'postgresql://{PG_USER}@{ip}/{DATABASE}'