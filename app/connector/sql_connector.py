from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_type = os.getenv('DATABASE_TYPE')
db_host = os.getenv('DATABASE_HOST')
db_name = os.getenv('DATABASE_NAME')
db_port = os.getenv('DATABASE_PORT')
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')

engine = create_engine(f'{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

connection = engine.connect()
Session = sessionmaker(connection)

print(f'connected to sql database {db_host}')