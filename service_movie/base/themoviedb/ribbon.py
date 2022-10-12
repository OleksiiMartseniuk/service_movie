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
