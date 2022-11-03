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
