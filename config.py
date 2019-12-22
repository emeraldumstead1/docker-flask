import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTRGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URL = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'