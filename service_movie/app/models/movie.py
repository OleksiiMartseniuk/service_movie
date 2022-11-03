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
