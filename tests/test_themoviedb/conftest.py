import pytest

from service_movie.base.themoviedb.api import TheMovieDatabaseApi
from service_movie.base.themoviedb.ribbon import MovieApi


@pytest.fixture()
def client_movie():
    client_movie = MovieApi(token='test_token')
    return client_movie


@pytest.fixture()
def client_api():
    client_api = TheMovieDatabaseApi(api_key='test_token')
    return client_api
