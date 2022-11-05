import sqlalchemy


metadata = sqlalchemy.MetaData()


# Таблица жанров
genres = sqlalchemy.Table(
    "genres",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_genes", sqlalchemy.Integer()),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
)


# Таблица производственные компании
production_companies = sqlalchemy.Table(
    "production_companies",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_companies", sqlalchemy.Integer(), nullable=False),
    sqlalchemy.Column("name", sqlalchemy.String(150), nullable=False),
    sqlalchemy.Column("logo_path", sqlalchemy.String(255)),
    sqlalchemy.Column("origin_country", sqlalchemy.String(255)),
)


# Таблица страны производства
production_countries = sqlalchemy.Table(
    "production_countries",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("iso_3166_1", sqlalchemy.String(150)),
    sqlalchemy.Column("name", sqlalchemy.String(150)),
)


# m2m таблица фильмов и жанров
movie_genre = sqlalchemy.Table(
    "movie_genre",
    metadata,
    sqlalchemy.Column("movie_id", sqlalchemy.ForeignKey("movies.id")),
    sqlalchemy.Column("genre_id", sqlalchemy.ForeignKey("genres.id")),
)


# m2m таблица фильмов и страны производства
movie_production_countries = sqlalchemy.Table(
    "movie_production_countries",
    metadata,
    sqlalchemy.Column("movie_id", sqlalchemy.ForeignKey("movies.id")),
    sqlalchemy.Column(
        "production_countries_id",
        sqlalchemy.ForeignKey("production_countries.id")
    ),
)


# m2m таблица фильмов и производственные компании
movie_production_companies = sqlalchemy.Table(
    "movie_production_companies",
    metadata,
    sqlalchemy.Column("movie_id", sqlalchemy.ForeignKey("movies.id")),
    sqlalchemy.Column(
        "production_companies_id",
        sqlalchemy.ForeignKey("production_companies.id")
    ),
)


# Таблица фильмов
movie = sqlalchemy.Table(
    "movies",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_movie", sqlalchemy.Integer(), index=True),
    sqlalchemy.Column("title", sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column("adult", sqlalchemy.Boolean()),
    sqlalchemy.Column("backdrop_path", sqlalchemy.String(255)),
    sqlalchemy.Column("budget", sqlalchemy.Integer()),
    sqlalchemy.Column("homepage", sqlalchemy.String(255)),
    sqlalchemy.Column("imdb_id", sqlalchemy.String(50)),
    sqlalchemy.Column("original_language", sqlalchemy.String(255)),
    sqlalchemy.Column("original_title", sqlalchemy.String(255)),
    sqlalchemy.Column("overview", sqlalchemy.Text()),
    sqlalchemy.Column("original_title", sqlalchemy.String(255)),
    sqlalchemy.Column("popularity", sqlalchemy.Float()),
    sqlalchemy.Column("poster_path", sqlalchemy.String(255)),
    sqlalchemy.Column("release_date", sqlalchemy.Date()),
    sqlalchemy.Column("revenue", sqlalchemy.Integer()),
    sqlalchemy.Column("runtime", sqlalchemy.Integer()),
    sqlalchemy.Column("status", sqlalchemy.String(100)),
    sqlalchemy.Column("tagline", sqlalchemy.String(255)),
    sqlalchemy.Column("video", sqlalchemy.Boolean()),
    sqlalchemy.Column("vote_average", sqlalchemy.Float()),
    sqlalchemy.Column("vote_count", sqlalchemy.Integer()),
    # production_companies m2m
    # production_countries m2m
    # genres m2m
)


# Таблица последняя серия в эфире
last_episode_to_air = sqlalchemy.Table(
    "last_episode_to_air",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_air", sqlalchemy.Integer()),
    sqlalchemy.Column("air_date", sqlalchemy.Date()),
    sqlalchemy.Column("episode_number", sqlalchemy.Integer()),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("overview", sqlalchemy.Text()),
    sqlalchemy.Column("production_code", sqlalchemy.String(50)),
    sqlalchemy.Column("season_number", sqlalchemy.Integer()),
    sqlalchemy.Column("still_path", sqlalchemy.String(255)),
    sqlalchemy.Column("vote_average", sqlalchemy.Float()),
    sqlalchemy.Column("vote_count", sqlalchemy.Integer()),
)


# Таблица сети
networks = sqlalchemy.Table(
    "networks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_network", sqlalchemy.Integer()),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("logo_path", sqlalchemy.String(255)),
    sqlalchemy.Column("origin_country", sqlalchemy.String(20)),
)


# Таблица сезон
seasons = sqlalchemy.Table(
    "seasons",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_seasons", sqlalchemy.Integer()),
    sqlalchemy.Column("air_date", sqlalchemy.Date()),
    sqlalchemy.Column("episode_count", sqlalchemy.Integer()),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("overview", sqlalchemy.Text()),
    sqlalchemy.Column("poster_path", sqlalchemy.String(255)),
    sqlalchemy.Column("season_number", sqlalchemy.Integer()),
)


# Таблица разговорные языки
spoken_languages = sqlalchemy.Table(
    "spoken_languages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("english_name", sqlalchemy.String(30)),
    sqlalchemy.Column("iso_639_1", sqlalchemy.String(20)),
    sqlalchemy.Column("name", sqlalchemy.String(30)),
)


# m2m таблица сериал и жанров
tv_genre = sqlalchemy.Table(
    "tv_genre",
    metadata,
    sqlalchemy.Column("tv_id", sqlalchemy.ForeignKey("tv.id")),
    sqlalchemy.Column("genre_id", sqlalchemy.ForeignKey("genres.id")),
)


# m2m таблица сериал и сети
tv_networks = sqlalchemy.Table(
    "tv_networks",
    metadata,
    sqlalchemy.Column("tv_id", sqlalchemy.ForeignKey("tv.id")),
    sqlalchemy.Column("network_id", sqlalchemy.ForeignKey("networks.id")),
)


# m2m таблица сериал и страны производства
tv_production_countries = sqlalchemy.Table(
    "tv_production_countries",
    metadata,
    sqlalchemy.Column("tv_id", sqlalchemy.ForeignKey("tv.id")),
    sqlalchemy.Column(
        "production_countries_id",
        sqlalchemy.ForeignKey("production_countries.id")
    ),
)


# m2m таблица сериал и производственные компании
tv_production_companies = sqlalchemy.Table(
    "tv_production_companies",
    metadata,
    sqlalchemy.Column("tv_id", sqlalchemy.ForeignKey("tv.id")),
    sqlalchemy.Column(
        "production_companies_id",
        sqlalchemy.ForeignKey("production_companies.id")
    ),
)


# m2m таблица сериал и сезон
tv_seasons = sqlalchemy.Table(
    "tv_seasons",
    metadata,
    sqlalchemy.Column("tv_id", sqlalchemy.ForeignKey("tv.id")),
    sqlalchemy.Column("seasons_id", sqlalchemy.ForeignKey("seasons.id")),
)


# m2m таблица сериал и разговорные языки
tv_spoken_languages = sqlalchemy.Table(
    "tv_spoken_languages",
    metadata,
    sqlalchemy.Column("tv_id", sqlalchemy.ForeignKey("tv.id")),
    sqlalchemy.Column(
        "spoken_languages_id",
        sqlalchemy.ForeignKey("spoken_languages.id")
    ),
)


# Таблица сериал
tv = sqlalchemy.Table(
    "tv",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("id_tv", sqlalchemy.Integer()),
    sqlalchemy.Column("backdrop_path", sqlalchemy.String(255)),
    # list[int] episode_run_time
    sqlalchemy.Column("episode_run_time", sqlalchemy.Integer()),
    sqlalchemy.Column("first_air_date", sqlalchemy.Date()),
    sqlalchemy.Column("homepage", sqlalchemy.String(255)),
    sqlalchemy.Column("in_production", sqlalchemy.Boolean()),
    # list[str] languages
    sqlalchemy.Column("languages", sqlalchemy.String(255)),
    sqlalchemy.Column("last_air_date", sqlalchemy.Date()),
    sqlalchemy.Column(
        "last_episode_to_air",
        sqlalchemy.ForeignKey('last_episode_to_air.id')
    ),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("number_of_episodes", sqlalchemy.Integer()),
    sqlalchemy.Column("number_of_seasons", sqlalchemy.Integer()),
    # list[str] origin_country
    sqlalchemy.Column("origin_country", sqlalchemy.String(255)),
    sqlalchemy.Column("original_language", sqlalchemy.String(20)),
    sqlalchemy.Column("original_name", sqlalchemy.String(255)),
    sqlalchemy.Column("overview", sqlalchemy.Text()),
    sqlalchemy.Column("popularity", sqlalchemy.Float()),
    sqlalchemy.Column("poster_path", sqlalchemy.String(255)),
    sqlalchemy.Column("status", sqlalchemy.String(100)),
    sqlalchemy.Column("tagline", sqlalchemy.String(255)),
    sqlalchemy.Column("type", sqlalchemy.String(100)),
    sqlalchemy.Column("vote_average", sqlalchemy.Float()),
    sqlalchemy.Column("vote_count", sqlalchemy.Integer()),
    # genres m2m
    # networks m2m
    # production_companies m2m
    # production_countries m2m
    # seasons m2m
    # spoken_languages m2m
)
