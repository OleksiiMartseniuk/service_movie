import logging
import asyncio

from enum import Enum

from .src.api import TheMovieDatabaseApi
from .src.validation import get_schemas_list
from .src import schemas


logger = logging.getLogger(__name__)


class ActionEnum(Enum):
    """Перечисление actions"""
    top_rating_movie = 'TopRatingMovie'
    popular_movie = 'PopularMovie'
    upcoming_movie = 'UpcomingMovie'
    top_rating_tv = 'TopRatingTV'
    popular_tv = 'PopularTV'


class MovieApi:
    """Получения данных"""

    def __init__(self, token: str) -> None:
        self.client = TheMovieDatabaseApi(api_key=token)

    def __get_link_method(self, action: ActionEnum):
        """Получить ссылку на функцию"""
        match action.value:
            case 'TopRatingMovie':
                func = self.client.get_top_rating_movie
            case 'PopularMovie':
                func = self.client.get_popular_movie
            case 'UpcomingMovie':
                func = self.client.get_upcoming_movie
            case 'TopRatingTV':
                func = self.client.get_top_rating_tv
            case 'PopularTV':
                func = self.client.get_popular_tv
            case _:
                logger.error(f'Неверный action[{action}]')
                return None
        return func

    async def get_genres(
        self, tv: bool = False
    ) -> list[schemas.Genre | None] | None:
        """Получения жанров"""
        data = await self.client.get_genres(tv=tv)

        if not data:
            logger.error('Нет данных жанров')
            return None

        try:
            genres = data['genres']
        except KeyError:
            logger.error('Нет ключа [genres]')
            return None

        return get_schemas_list(genres, schemas.Genre)

    async def get_count_page(
        self, action: ActionEnum, region: str = 'RU'
    ) -> int | None:
        """Получения количества страниц"""
        func = self.__get_link_method(action=action)

        if not func:
            return None

        data = await func(region=region)

        if not data:
            logger.error(f'Нет данных [{func.__name__}]')
            return None

        try:
            count = data['total_pages']
        except KeyError:
            logger.error('Нет ключа [total_pages]')
            return None
        return count
