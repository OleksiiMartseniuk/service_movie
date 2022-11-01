import pytest
import httpx

from . import config_data


@pytest.mark.asyncio
async def test_get(mocker, client_api):
    mocker.patch(
        'service_movie.base.themoviedb.api.httpx.AsyncClient.get',
        return_value=httpx.Response(200, json={'test': 'test'})
    )
    result = await client_api.get('https://test-api')
    assert result == {'test': 'test'}


@pytest.mark.asyncio
@pytest.mark.parametrize('status_code', [300, 400, 500])
async def test_get_status_code(status_code, mocker, client_api):
    mocker.patch(
        'service_movie.base.themoviedb.api.httpx.AsyncClient.get',
        return_value=httpx.Response(status_code, json={'error': 'error'})
    )
    result = await client_api.get('https://test-api')
    assert result is None


@pytest.mark.asyncio
@pytest.mark.parametrize('tv', [True, False])
async def test_get_genres(tv, mocker, client_api):
    mocker.patch(
        'service_movie.base.themoviedb.api.TheMovieDatabaseApi.get',
        return_value=config_data.genres
    )
    result = await client_api.get_genres(tv=tv)
    assert config_data.genres == result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'params, result',
    [
        ({}, config_data.params_default),
        (config_data.params_data, config_data.params_result)
    ]
)
async def test_set_params(params, result, client_api):
    params_result = await client_api._set_params(**params)
    assert params_result == result
