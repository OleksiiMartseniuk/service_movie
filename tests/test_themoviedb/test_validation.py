from service_movie.base.themoviedb import validation, schemas

from . import config_data


def test_get_schemas():
    data = validation.get_schemas(
        data=config_data.genres,
        schema_model=schemas.Genres
    )
    assert data == config_data.genres_schema


def test_get_schemas_not_validation():
    data = validation.get_schemas(
        data={'genre_1': 'one', 'genre_2': 'two'},
        schema_model=schemas.Genres
    )
    assert data is None
