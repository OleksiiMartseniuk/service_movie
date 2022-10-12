import logging

from .src.api import TheMovieDatabaseApi
from .src.validation import get_schemas
from .src import schemas


logger = logging.getLogger(__name__)


class MovieApi:
    """Получения данных"""

    def __init__(self, token: str) -> None:
        self.client = TheMovieDatabaseApi(api_key=token)

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

        result = []
        for genre in genres:
            item = get_schemas(genre, schemas.Genre)
            if item:
                result.append(item)
        return result

    async def _get_count_page(
        self, action: int, region: str = 'RU'
    ) -> int | None:
        """Получения количества страниц"""
        match action:
            case 1:
                data = await self.client.get_top_rating_movie(region=region)
            case 2:
                data = await self.client.get_popular_movie(region=region)
            case 3:
                data = await self.client.get_upcoming_movie(region=region)
            case 4:
                data = await self.client.get_top_rating_tv()
            case 5:
                data = await self.client.get_popular_tv()
            case _:
                logger.error(f'Неверный action[{action}]')
                return None

        if not data:
            logger.error(f'Нет данных action[{action}]')
            return None

        try:
            count = data['total_pages']
        except KeyError:
            logger.error('Нет ключа [total_pages]')
            return None
        return count
