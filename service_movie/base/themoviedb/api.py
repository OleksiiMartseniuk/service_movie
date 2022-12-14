import httpx
import logging
import asyncio


logger = logging.getLogger(__name__)


class TheMovieDatabaseApi:
    """Api client"""

    def __init__(
        self,
        api_key: str,
        url: str = "https://api.themoviedb.org/",
        version: int = 3,
        language: str = 'ru-Ru',
        response_count: int = 10
    ) -> None:
        self.url = url + str(version)
        self.api_key = api_key
        self.language = language
        self.limit = asyncio.Semaphore(response_count)

    async def get(self, url: str, **kwargs) -> dict | None:
        async with (self.limit, httpx.AsyncClient() as client):
            try:
                response = await client.get(url=url, **kwargs)
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(f'status_code [{response.status_code}] '
                                 f'error_message [{response.json()}]')
                    return None
            except httpx.RequestError as exc:
                logger.error(f'{exc.__class__}-{str(exc)}')
                return None

    async def _set_params(self, **kwargs) -> dict:
        """Формирования параметров"""
        params_default = {
            'api_key': self.api_key,
            'language': self.language,
        }
        if kwargs:
            # Добавляем только те параметры которые имеют значения
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
        url = f'{self.url}/movie/top_rated'
        params = await self._set_params(page=page, region=region)
        return await self.get(url=url, params=params)

    async def get_popular_movie(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """
        Получите список текущих популярных фильмов.
        Этот список обновляется ежедневно.
        """
        url = f'{self.url}/movie/popular'
        params = await self._set_params(page=page, region=region)
        return await self.get(url=url, params=params)

    async def get_upcoming_movie(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """Получить список предстоящих фильмов в кинотеатрах."""
        url = f'{self.url}/movie/upcoming'
        params = await self._set_params(page=page, region=region)
        return await self.get(url=url, params=params)

    async def get_top_rating_tv(self, page: int = 1, **kwargs):
        """Получите список телешоу с самым высоким рейтингом"""
        url = f'{self.url}/tv/top_rated'
        params = await self._set_params(page=page)
        return await self.get(url=url, params=params)

    async def get_popular_tv(self, page: int = 1, **kwargs):
        """
        Получите список текущих популярных телешоу.
        Этот список обновляется ежедневно.
        """
        url = f'{self.url}/tv/popular'
        params = await self._set_params(page=page)
        return await self.get(url=url, params=params)

    async def get_languages(self) -> list[dict] | None:
        """Получите список языков"""
        url = f'{self.url}/configuration/languages'
        params = await self._set_params()
        return await self.get(url=url, params=params)

    async def get_countries(self) -> list[dict] | None:
        """Получить список стран"""
        url = f'{self.url}/configuration/countries'
        params = await self._set_params()
        return await self.get(url=url, params=params)

    async def get_recommendations(
        self, item: str, id: int, page: int = 1
    ) -> dict | None:
        """Получить список рекомендуемых телешоу/фильмов для этого элемента

        Parameters
        ----------
        item : str
            [movie] Выбрать список фильмов
            [tv] Выбрать список телешоу/фильмов
        id : int
            ID телешоу/фильмов
        page : int
            Номер страницы
        """
        item_list = ['movie', 'tv']

        if item not in item_list:
            logger.error(f'Неверный item[{item}]')
            return None

        url = f'{self.url}/{item}/{id}/recommendations'
        params = await self._set_params(page=page)
        return await self.get(url=url, params=params)

    async def get_trending(self, media_type: str, time_window: str) -> dict:
        """Получайте ежедневные или еженедельные трендовые товары

        Parameters
        ----------
        media_type : str
            [movie] Показать популярные фильмы в результатах
            [tv] Показать популярные телешоу в результатах
        time_window : str
            [day] Просмотрите список трендов дня
            [week] Посмотреть список трендов на неделю
        """
        media_type_list = ['movie', 'tv']
        time_window_list = ['day', 'week']

        if media_type not in media_type_list:
            logger.error(f'Неверный media_type[{media_type}]')
            return None

        if time_window not in time_window_list:
            logger.error(f'Неверный time_window[{time_window}]')
            return None

        url = f'{self.url}/trending/{media_type}/{time_window}'
        params = await self._set_params()
        return await self.get(url=url, params=params)
