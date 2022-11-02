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
        config_data.mock_path_get,
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


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'tv, response, id',
    [
        (True, config_data.tv, 72925),
        (False, config_data.movie, 331)
    ]
)
async def test_get_details(tv, response, id, mocker, client_api):
    mocker.patch(
        config_data.mock_path_get,
        return_value=response
    )
    result = await client_api.get_details(id=id, tv=tv)
    assert result == response


@pytest.mark.asyncio
async def test_get_top_rating_movie(mocker, client_api):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.top_rating_movie
    )
    result = await client_api.get_top_rating_movie()
    assert result == config_data.top_rating_movie


@pytest.mark.asyncio
async def test_get_popular_movie(mocker, client_api):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.popular_movie
    )
    result = await client_api.get_popular_movie()
    assert result == config_data.popular_movie


@pytest.mark.asyncio
async def test_get_upcoming_movie(mocker, client_api):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.upcoming_movie
    )
    result = await client_api.get_upcoming_movie()
    assert result == config_data.upcoming_movie


@pytest.mark.asyncio
async def test_get_top_rating_tv(mocker, client_api):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.top_rating_tv
    )
    result = await client_api.get_top_rating_tv()
    assert result == config_data.top_rating_tv


@pytest.mark.asyncio
async def test_get_popular_tv(mocker, client_api):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.popular_tv
    )
    result = await client_api.get_popular_tv()
    assert result == config_data.popular_tv
