import logging

from typing import TypeVar, Type

from pydantic import BaseModel, ValidationError


logger = logging.getLogger(__name__)
ModelSchemaType = TypeVar('ModelSchemaType', bound=BaseModel)


def get_schemas(
    data: dict,
    schema_model: Type[ModelSchemaType]
) -> BaseModel | None:
    """Получения схемы"""
    try:
        result = schema_model(**data)
    except ValidationError as exc:
        logger.error(f'{exc.__class__} {str(exc)}')
        return None
    return result
