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

    async def get_details(self, movie_id: int) -> dict | None:
        """Получить первичную информацию о фильме"""
        url = self.url + f'/movie/{movie_id}'
        params = {'api_key': self.api_key, 'language': self.language}
        return await self.get(url=url, params=params)

    async def get_top_rating(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """Получите фильмы с самым высоким рейтингом"""
        url = self.url + '/movie/top_rated'
        params = {
            'api_key': self.api_key,
            'language': self.language,
            'page': page,
        }
        if region:
            params['region'] = region
        return await self.get(url=url, params=params)

    async def get_popular(
        self, page: int = 1, region: str = None
    ) -> dict | None:
        """
        Получите список текущих популярных фильмов.
        Этот список обновляется ежедневно.
        """
        url = self.url + '/movie/popular'
        params = {
            'api_key': self.api_key,
            'language': self.language,
            'page': page
        }
        if region:
            params['region'] = region
        return await self.get(url=url, params=params)


async def main():
    client = TheMovieDatabaseApi('04d75758a71fdfab2b612a1154cda34f')
    a = await client.get_popular()
    print(a)

asyncio.run(main())
