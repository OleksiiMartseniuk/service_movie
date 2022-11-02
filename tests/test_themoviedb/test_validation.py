import pytest

from service_movie.base.themoviedb import validation, schemas

from . import config_data


@pytest.mark.parametrize(
    'data, schema_model, result',
    [
        (config_data.genres, schemas.Genres, config_data.genres_schema),
        (config_data.movie, schemas.Movie, config_data.movie_schema),
        (config_data.tv, schemas.TV, config_data.tv_schema),
    ]
)
def test_get_schemas(data, schema_model, result):
    result_data = validation.get_schemas(
        data=data,
        schema_model=schema_model
    )
    assert result_data == result


@pytest.mark.parametrize(
    'data, schema_model',
    [
        (config_data.genres, schemas.TV),
        (config_data.movie, schemas.MovieResult),
        (config_data.tv, schemas.TopRatedTV),
    ]
)
def test_get_schemas_not_validation(data, schema_model):
    result = validation.get_schemas(
        data=data,
        schema_model=schema_model
    )
    assert result is None
