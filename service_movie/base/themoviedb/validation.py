import logging

from pydantic import ValidationError

from .schemas import Genre


logger = logging.getLogger(__name__)


def get_genres_schemas(data: dict) -> list[Genre] | None:
    """Получения списка схемы Genre"""
    try:
        genres: list = data['genres']
    except KeyError:
        logger.error('Нет данных')
        return None

    try:
        genres_schema = [Genre(**genre) for genre in genres]
    except ValidationError as exc:
        logger.error(f'{exc.__class__}-{str(exc)}')
        return None

    return genres_schema
