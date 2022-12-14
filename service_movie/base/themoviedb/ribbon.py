import logging
import asyncio

from enum import Enum
from pydantic import BaseModel

from .api import TheMovieDatabaseApi
from .validation import get_schemas
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
    TOP_RATING_MOVIE = ('top_rating_movie', schemas.TopRatingMovieList)
    POPULAR_MOVIE = ('popular_movie', schemas.PopularMovieList)
    UPCOMING_MOVIE = ('upcoming_movie', schemas.UpcomingMovieList)
    TOP_RATING_TV = ('top_rating_tv', schemas.TopRatedTVList)
    POPULAR_TV = ('popular_tv', schemas.PopularTVList)

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

    def __get_schema_base(
        self, item: str
    ) -> schemas.BaseMovieResult | schemas.BaseTVResult:
        """Получаем основною схему tv/movie"""
        if item == 'movie':
            return schemas.BaseMovieResult
        elif item == 'tv':
            return schemas.BaseTVResult

    async def __get_count_page(
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
        # Ограничения количество страниц не больше 500
        if count > 500:
            count = 500

        return count

    async def get_details(
        self, id: int, tv: bool = False
    ) -> schemas.Movie | schemas.TV | None:
        """
        Получить первичную информацию о фильме/сериалов
        Default [получения информацию о фильме]
        tv = True [получения информацию о сериалов]
        """
        data = await self.client.get_details(id=id, tv=tv)

        if not data:
            logger.error(f'Нет данных get_details[id={id}, tv={tv}]')
            return None

        schema = schemas.TV if tv else schemas.Movie

        return get_schemas(data, schema)

    async def get_genres(self, tv: bool = False) -> schemas.Genres | None:
        """Получения жанров"""
        data = await self.client.get_genres(tv=tv)

        if not data:
            logger.error('Нет данных жанров')
            return None

        return get_schemas(data, schemas.Genres)

    async def get_languages(self) -> schemas.SpokenLanguagesList | None:
        """Получите список языков"""
        data = await self.client.get_languages()

        if not data:
            logger.error('Нет данных get_languages')
            return None

        return get_schemas({'data': data}, schemas.SpokenLanguagesList)

    async def get_countries(self) -> schemas.CountriesList | None:
        """Получить список стран"""
        data = await self.client.get_countries()

        if not data:
            logger.error('Нет данных get_countries')
            return None

        return get_schemas({'data': data}, schemas.CountriesList)

    async def get_data(
        self, item: ActionEnum, region: str = None
    ) -> BaseModel | None:
        """Получения списка данных фильмов/TV"""
        count = await self.__get_count_page(item=item, region=region)
        if not count:
            logger.error('Нет данных о количеству страниц')
            return None

        func = self.__get_link_method(item=item)

        # Создания списка задач
        tasks = []
        for page in range(1, count + 1):
            task = asyncio.create_task(func(page=page, region=region))
            tasks.append(task)
        data_list = await asyncio.gather(*tasks)
        return get_schemas({'data': data_list},  item.schema)

    async def get_recommendations(
        self, item: str, id: int, page: int = 1
    ) -> schemas.BaseMovieResult | schemas.BaseTVResult | None:
        """Получить список рекомендуемых телешоу/фильмов для этого элемента"""
        data = await self.client.get_recommendations(item, id, page)

        if not data:
            logger.error('Нет данных get_recommendations'
                         f'(item-{item}id-{id}, page-{page})')
            return None

        schema = self.__get_schema_base(item=item)

        return get_schemas(data, schema)

    async def get_trending(
        self, media_type: str, time_window: str
    ) -> schemas.BaseMovieResult | schemas.BaseTVResult | None:
        """Получайте ежедневные или еженедельные трендовые товары"""
        data = await self.client.get_trending(media_type, time_window)

        if not data:
            logger.error('Нет данных get_trending'
                         f'(media_type-{media_type}time_window-{time_window}')
            return None

        schema = self.__get_schema_base(item=media_type)

        return get_schemas(data, schema)
