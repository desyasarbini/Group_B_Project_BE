from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

engine = create_engine(f'{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')

connection = engine.connect()
Session = sessionmaker(connection)

print(f'connected to sql database {DATABASE_HOST}')