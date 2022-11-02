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
    ActionEnum.POPULAR_TV.action = 'actin'
    method = client_movie._MovieApi__get_link_method(ActionEnum.POPULAR_TV)
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
