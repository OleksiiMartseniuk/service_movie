from pydantic import BaseModel


class Genre(BaseModel):
    """Жанр"""
    id: int
    name: str


class Genres(BaseModel):
    """Жанры"""
    genres: list[Genre]


class ProductionCompanies(BaseModel):
    """Производственные компании"""
    name: str
    id: int
    logo_path: str | None
    origin_country: str


class ProductionCountries(BaseModel):
    """Страны производства"""
    iso_3166_1: str
    name: str


class Dates(BaseModel):
    """Дата"""
    maximum: str
    minimum: str


class Movie(BaseModel):
    """Фильм"""
    id: int
    title: str
    adult: bool
    backdrop_path: str | None
    budget: int
    genres: list[Genre]
    homepage: str | None
    imdb_id: str | None
    original_language: str
    original_title: str
    overview: str | None
    popularity: float
    poster_path: str | None
    production_companies: list[ProductionCompanies]
    production_countries: list[ProductionCountries]
    release_date: str
    revenue: int
    runtime: int | None
    status: str
    tagline: str | None
    video: bool
    vote_average: float
    vote_count: int


class MovieResult(BaseModel):
    """Фильм результат"""
    id: int
    title: str
    poster_path: str | None
    adult: bool
    overview: str
    release_date: str
    genre_ids: list[int]
    original_title: str
    original_language: str
    backdrop_path: str | None
    popularity: float
    vote_count: int
    video: bool
    vote_average: float


class BaseMovieResult(BaseModel):
    """Основной вывод результата фильмов"""
    page: int
    results: list[MovieResult]
    total_results: int
    total_pages: int


class TopRatingMovie(BaseMovieResult):
    """Фильмы с самым высоким рейтингом"""
    pass


class TopRatingMovieList(BaseModel):
    """Список фильмы с самым высоким рейтингом"""
    data: list[TopRatingMovie]


class PopularMovie(BaseMovieResult):
    """Популярный фильм"""
    pass


class PopularMovieList(BaseModel):
    """Список популярный фильм"""
    data: list[PopularMovie]


class UpcomingMovie(BaseMovieResult):
    """Предстоящий фильм в кинотеатрах"""
    dates: Dates


class UpcomingMovieList(BaseModel):
    """Список предстоящий фильм в кинотеатрах"""
    data: list[UpcomingMovie]


class CreatedBy(BaseModel):
    """Создания TV"""
    id: int
    credit_id: str
    name: str
    gender: int
    profile_path: str | None


class LastEpisodeToAir(BaseModel):
    """Последняя серия в эфире"""
    air_date: str
    episode_number: int
    id: int
    name: str
    overview: str
    production_code: str
    season_number: int
    still_path: str | None
    vote_average: float
    vote_count: int


class Networks(BaseModel):
    """Сети"""
    name: str
    id: int
    logo_path: str | None
    origin_country: str


class Seasons(BaseModel):
    """Времена года"""
    air_date: str | None
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: str | None
    season_number: int


class SpokenLanguages(BaseModel):
    """Разговорные языки"""
    english_name: str
    iso_639_1: str
    name: str


class TV(BaseModel):
    """Сериал"""
    backdrop_path: str | None
    created_by: list[CreatedBy]
    episode_run_time: list[int]
    first_air_date: str
    genres: list[Genre]
    homepage: str
    id: int
    in_production: bool
    languages: list[str]
    last_air_date: str
    last_episode_to_air: LastEpisodeToAir
    name: str
    networks: list[Networks]
    number_of_episodes: int
    number_of_seasons: int
    origin_country: list[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str | None
    production_companies: list[ProductionCompanies]
    production_countries: list[ProductionCountries]
    seasons: list[Seasons]
    spoken_languages: list[SpokenLanguages]
    status: str
    tagline: str
    type: str
    vote_average: float
    vote_count: int


class TVResult(BaseModel):
    """Сериал результат"""
    poster_path: str | None
    popularity: float
    id: int
    backdrop_path: str | None
    vote_average: float
    overview: str
    first_air_date: str
    origin_country: list[str]
    genre_ids: list[int]
    original_language: str
    vote_count: int
    name: str
    original_name: str


class BaseTVResult(BaseModel):
    """Основной вывод результата фильмов"""
    page: int
    results: list[TVResult]
    total_results: int
    total_pages: int


class PopularTV(BaseTVResult):
    """Популярные телешоу"""
    pass


class PopularTVList(BaseModel):
    """Список популярные телешоу"""
    data: list[PopularTV]


class TopRatedTV(BaseTVResult):
    """Телешоу с самым высоким рейтингом"""
    pass


class TopRatedTVList(BaseModel):
    """Список телешоу с самым высоким рейтингом"""
    data: list[TopRatedTV]
