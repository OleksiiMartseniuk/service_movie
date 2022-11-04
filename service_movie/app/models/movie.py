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
