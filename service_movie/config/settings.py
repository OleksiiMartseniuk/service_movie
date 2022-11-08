import os

# DataBase
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'\
    f'@{HOST_DB}:{PORT_DB}/{POSTGRES_DB}'
TEST_SQLALCHEMY_DATABASE_URL = ''

# Key TheMovieDB
API_KEY_THE_MOVIE_DB = os.getenv('API_KEY_THE_MOVIE_DB')

# Testing app
TESTING = os.getenv('TESTING')

# Base path 'service_movie'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
