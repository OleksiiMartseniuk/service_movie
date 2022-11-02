import pytest

from service_movie.base.themoviedb.ribbon import ActionEnum


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

