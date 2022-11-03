import pytest

from service_movie.base.themoviedb.ribbon import ActionEnum

from . import config_data


def test_get_link_method(client_movie):
    method = client_movie._MovieApi__get_link_method(
        ActionEnum.TOP_RATING_MOVIE
    )
    assert method == client_movie.client.get_top_rating_movie

    method = client_movie._MovieApi__get_link_method(ActionEnum.POPULAR_MOVIE)
    assert method == client_movie.client.get_popular_movie

    method = client_movie._MovieApi__get_link_method(ActionEnum.UPCOMING_MOVIE)
    assert method == client_movie.client.get_upcoming_movie

    method = client_movie._MovieApi__get_link_method(ActionEnum.TOP_RATING_TV)
    assert method == client_movie.client.get_top_rating_tv

    method = client_movie._MovieApi__get_link_method(ActionEnum.POPULAR_TV)
    assert method == client_movie.client.get_popular_tv


def test_get_link_method_not_action(client_movie):
    method = client_movie._MovieApi__get_link_method(
        config_data.ActionTest.TEST_ITEM
    )
    assert method is None


@pytest.mark.asyncio
async def test_get_count_page(mocker, client_movie):
    page = 422
    data = config_data.popular_movie.copy()
    data['total_pages'] = page

    mocker.patch(config_data.mock_path_get, return_value=data)

    count = await client_movie._MovieApi__get_count_page(
        ActionEnum.POPULAR_MOVIE
    )
    assert count == page


@pytest.mark.asyncio
async def test_get_count_page_if_500(mocker, client_movie):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.popular_movie
    )

    count = await client_movie._MovieApi__get_count_page(
        ActionEnum.POPULAR_MOVIE
    )
    assert count == 500


@pytest.mark.asyncio
async def test_get_count_page_key_error(mocker, client_movie):
    mocker.patch(
        config_data.mock_path_get,
        return_value={'test': 'test'}
    )

    count = await client_movie._MovieApi__get_count_page(
        ActionEnum.POPULAR_MOVIE
    )
    assert count is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'id, tv, result, data',
    [
        (
            config_data.movie['id'],
            False, config_data.movie_schema,
            config_data.movie
        ),
        (
            config_data.tv['id'],
            True, config_data.tv_schema,
            config_data.tv
        )
    ]
)
async def test_get_details(id, tv, result, data, mocker, client_movie):
    mocker.patch(
        config_data.mock_path_get,
        return_value=data
    )

    result_data = await client_movie.get_details(id=id, tv=tv)
    assert result_data == result


@pytest.mark.asyncio
async def test_get_details_not_data(mocker, client_movie):
    mocker.patch(config_data.mock_path_get, return_value=None)

    result_data = await client_movie.get_details(id=1)
    assert result_data is None


@pytest.mark.asyncio
@pytest.mark.parametrize('tv', [True, False])
async def test_get_genres(tv, mocker, client_movie):
    mocker.patch(
        config_data.mock_path_get,
        return_value=config_data.genres
    )

    result = await client_movie.get_genres(tv=tv)
    assert result == config_data.genres_schema


@pytest.mark.asyncio
async def test_get_genres_not_data(mocker, client_movie):
    mocker.patch(config_data.mock_path_get, return_value=None)

    result = await client_movie.get_genres()
    assert result is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'data, action, result',
    [
        (
            config_data.popular_movie,
            ActionEnum.POPULAR_MOVIE,
            config_data.popular_movie_list_schema
        ),
        (
            config_data.popular_tv,
            ActionEnum.POPULAR_TV,
            config_data.popular_tv_list_schema
        ),
        (
            config_data.top_rating_movie,
            ActionEnum.TOP_RATING_MOVIE,
            config_data.top_rating_movie_list_schema
        ),
        (
            config_data.top_rating_tv,
            ActionEnum.TOP_RATING_TV,
            config_data.top_rating_tv_list_schema
        ),
        (
            config_data.upcoming_movie,
            ActionEnum.UPCOMING_MOVIE,
            config_data.upcoming_movie_list_schema
        ),
    ]
)
async def test_get_data(data, action, result, mocker, client_movie):
    mocker.patch(
        config_data.mock_path_get,
        return_value=data
    )

    result_data = await client_movie.get_data(action)
    assert result_data == result


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'action',
    [
        ActionEnum.POPULAR_MOVIE,
        ActionEnum.POPULAR_TV,
        ActionEnum.TOP_RATING_MOVIE,
        ActionEnum.TOP_RATING_TV,
        ActionEnum.UPCOMING_MOVIE
    ]
)
async def test_get_data_not_count(action, mocker, client_movie):
    mocker.patch(
        config_data.mock_path_get_count_page,
        return_value=None
    )
    mock_get_link_method = mocker.patch(config_data.mock_get_link_method)
    result = await client_movie.get_data(action)

    assert result is None
    mock_get_link_method.assert_not_called()
