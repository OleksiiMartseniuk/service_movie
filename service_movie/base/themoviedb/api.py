import httpx
import logging


logger = logging.getLogger(__name__)


class TheMovieDatabaseApi:
    """Api client"""

    def __init__(
        self,
        api_key: str,
        url: str = "https://api.themoviedb.org/",
        version: int = 3,
        language: str = 'ru-Ru'
    ) -> None:
        self.url = url + str(version)
        self.api_key = api_key
        self.language = language

    async def get(self, url: str, **kwargs) -> dict | None:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url=url, **kwargs)
                if response.status_code == 200:
                    return response.json()
            except httpx.RequestError as exc:
                logger.error(f'{exc.__class__}-{str(exc)}')

    async def _set_params(self, **kwargs) -> dict:
        """Формирования параметров"""
        params_default = {
            'api_key': self.api_key,
            'language': self.language,
        }
        if kwargs:
            params = {key: value for key, value in kwargs.items() if value}
            params_default.update(params)
        return params_default

    async def get_genres(self, tv: bool = False) -> dict | None:
        """
        Получите список официальных жанров фильмов/сериалов.
        Default [получения жанров фильмов]
        tv = True [получения жанров сериалов]
        """
        path = '/genre/tv/list' if tv else '/genre/movie/list'
        url = self.url + path
        params = await self._set_params()
        return await self.get(url=url, params=params)

    async def get_details(
        self, id: int, tv: bool = False
    ) -> dict | None:
        """
        Получить первичную информацию о фильме/сериалов
        Default [получения информацию о фильме]
        tv = True [получения информацию о сериалов]
        """
        path = f'/tv/{id}' if tv else f'/movie/{id}'
        url = self.url + path
        params = await self._set_params()
        return await self.get(url=url, params=params)

    async def get_top_rating_movie(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """Получите фильмы с самым высоким рейтингом"""
        url = self.url + '/movie/top_rated'
        params = await self._set_params(page=page, region=region)
        return await self.get(url=url, params=params)

    async def get_popular_movie(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """
        Получите список текущих популярных фильмов.
        Этот список обновляется ежедневно.
        """
        url = self.url + '/movie/popular'
        params = await self._set_params(page=page, region=region)
        return await self.get(url=url, params=params)

    async def get_upcoming_movie(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """Получить список предстоящих фильмов в кинотеатрах."""
        url = self.url + '/movie/upcoming'
        params = await self._set_params(page=page, region=region)
        return await self.get(url=url, params=params)
