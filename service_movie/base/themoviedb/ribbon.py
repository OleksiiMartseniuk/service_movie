import logging
import asyncio

from enum import Enum
from pydantic import BaseModel

from .api import TheMovieDatabaseApi
from .validation import get_schemas_list
from . import schemas

logger = logging.getLogger(__name__)


class ActionEnum(Enum):
    """
    Перечисление actions
    ---
    TOP_RATING_MOVIE: Фильмы с самым высоким рейтингом
    POPULAR_MOVIE: Список текущих популярных фильмов
    UPCOMING_MOVIE: Список предстоящих фильмов в кинотеатрах
    TOP_RATING_TV: Телешоу с самым высоким рейтингом
    POPULAR_TV: Список текущих популярных телешоу
    """
    TOP_RATING_MOVIE = ('top_rating_movie', schemas.TopRatingMovie)
    POPULAR_MOVIE = ('popular_movie', schemas.PopularMovie)
    UPCOMING_MOVIE = ('upcoming_movie', schemas.UpcomingMovie)
    TOP_RATING_TV = ('top_rating_tv', schemas.TopRatedTV)
    POPULAR_TV = ('popular_tv', schemas.PopularTV)

    def __init__(self, action: str, schema: BaseModel) -> None:
        self.action = action
        self.schema = schema


class MovieApi:
    """Получения данных"""

    def __init__(self, token: str, **kwargs) -> None:
        self.client = TheMovieDatabaseApi(api_key=token, **kwargs)

    def __get_link_method(self, item: ActionEnum):
        """Получить ссылку на функцию"""
        match item.action:
            case 'top_rating_movie':
                func = self.client.get_top_rating_movie
            case 'popular_movie':
                func = self.client.get_popular_movie
            case 'upcoming_movie':
                func = self.client.get_upcoming_movie
            case 'top_rating_tv':
                func = self.client.get_top_rating_tv
            case 'popular_tv':
                func = self.client.get_popular_tv
            case _:
                logger.error(f'Неверный action[{item}]')
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
        self, item: ActionEnum, region: str = None
    ) -> int | None:
        """Получения количества страниц"""
        func = self.__get_link_method(item=item)

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

    async def get_data(
        self, item: ActionEnum, region: str = None
    ) -> list[BaseModel | None] | None:
        """Получения списка данных фильмов/TV"""
        count = await self.get_count_page(item=item, region=region)

        if not count:
            logger.error('Нет данных о количеству страниц')
            return None

        func = self.__get_link_method(item=item)

        if not func:
            return None

        # Создания списка задач
        tasks = []
        for page in range(1, count + 1):
            task = asyncio.create_task(func(page=page, region=region))
            tasks.append(task)
        data_list = await asyncio.gather(*tasks)

        return get_schemas_list(data_list,  item.schema)
