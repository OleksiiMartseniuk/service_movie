"""Added required tables

Revision ID: 78c95bd1adc0
Revises: 
Create Date: 2022-11-05 17:10:05.240192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78c95bd1adc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_genes', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('last_episode_to_air',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_air', sa.Integer(), nullable=True),
    sa.Column('air_date', sa.Date(), nullable=True),
    sa.Column('episode_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('production_code', sa.String(length=50), nullable=True),
    sa.Column('season_number', sa.Integer(), nullable=True),
    sa.Column('still_path', sa.String(length=255), nullable=True),
    sa.Column('vote_average', sa.Float(), nullable=True),
    sa.Column('vote_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_movie', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('adult', sa.Boolean(), nullable=True),
    sa.Column('backdrop_path', sa.String(length=255), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('homepage', sa.String(length=255), nullable=True),
    sa.Column('imdb_id', sa.String(length=50), nullable=True),
    sa.Column('original_language', sa.String(length=255), nullable=True),
    sa.Column('original_title', sa.String(length=255), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('popularity', sa.Float(), nullable=True),
    sa.Column('poster_path', sa.String(length=255), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('revenue', sa.Integer(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('tagline', sa.String(length=255), nullable=True),
    sa.Column('video', sa.Boolean(), nullable=True),
    sa.Column('vote_average', sa.Float(), nullable=True),
    sa.Column('vote_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movies_id_movie'), 'movies', ['id_movie'], unique=False)
    op.create_table('networks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_network', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('logo_path', sa.String(length=255), nullable=True),
    sa.Column('origin_country', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('production_companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_companies', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('logo_path', sa.String(length=255), nullable=True),
    sa.Column('origin_country', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('production_countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iso_3166_1', sa.String(length=150), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_seasons', sa.Integer(), nullable=True),
    sa.Column('air_date', sa.Date(), nullable=True),
    sa.Column('episode_count', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('poster_path', sa.String(length=255), nullable=True),
    sa.Column('season_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spoken_languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('english_name', sa.String(length=30), nullable=True),
    sa.Column('iso_639_1', sa.String(length=20), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_genre',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], )
    )
    op.create_table('movie_production_companies',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('production_companies_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['production_companies_id'], ['production_companies.id'], )
    )
    op.create_table('movie_production_countries',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('production_countries_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['production_countries_id'], ['production_countries.id'], )
    )
    op.create_table('tv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_tv', sa.Integer(), nullable=True),
    sa.Column('backdrop_path', sa.String(length=255), nullable=True),
    sa.Column('episode_run_time', sa.Integer(), nullable=True),
    sa.Column('first_air_date', sa.Date(), nullable=True),
    sa.Column('homepage', sa.String(length=255), nullable=True),
    sa.Column('in_production', sa.Boolean(), nullable=True),
    sa.Column('languages', sa.String(length=255), nullable=True),
    sa.Column('last_air_date', sa.Date(), nullable=True),
    sa.Column('last_episode_to_air', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('number_of_episodes', sa.Integer(), nullable=True),
    sa.Column('number_of_seasons', sa.Integer(), nullable=True),
    sa.Column('origin_country', sa.String(length=255), nullable=True),
    sa.Column('original_language', sa.String(length=20), nullable=True),
    sa.Column('original_name', sa.String(length=255), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('popularity', sa.Float(), nullable=True),
    sa.Column('poster_path', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('tagline', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('vote_average', sa.Float(), nullable=True),
    sa.Column('vote_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['last_episode_to_air'], ['last_episode_to_air.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tv_genre',
    sa.Column('tv_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['tv_id'], ['tv.id'], )
    )
    op.create_table('tv_networks',
    sa.Column('tv_id', sa.Integer(), nullable=True),
    sa.Column('network_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['network_id'], ['networks.id'], ),
    sa.ForeignKeyConstraint(['tv_id'], ['tv.id'], )
    )
    op.create_table('tv_production_companies',
    sa.Column('tv_id', sa.Integer(), nullable=True),
    sa.Column('production_companies_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['production_companies_id'], ['production_companies.id'], ),
    sa.ForeignKeyConstraint(['tv_id'], ['tv.id'], )
    )
    op.create_table('tv_production_countries',
    sa.Column('tv_id', sa.Integer(), nullable=True),
    sa.Column('production_countries_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['production_countries_id'], ['production_countries.id'], ),
    sa.ForeignKeyConstraint(['tv_id'], ['tv.id'], )
    )
    op.create_table('tv_seasons',
    sa.Column('tv_id', sa.Integer(), nullable=True),
    sa.Column('seasons_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seasons_id'], ['seasons.id'], ),
    sa.ForeignKeyConstraint(['tv_id'], ['tv.id'], )
    )
    op.create_table('tv_spoken_languages',
    sa.Column('tv_id', sa.Integer(), nullable=True),
    sa.Column('spoken_languages_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['spoken_languages_id'], ['spoken_languages.id'], ),
    sa.ForeignKeyConstraint(['tv_id'], ['tv.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tv_spoken_languages')
    op.drop_table('tv_seasons')
    op.drop_table('tv_production_countries')
    op.drop_table('tv_production_companies')
    op.drop_table('tv_networks')
    op.drop_table('tv_genre')
    op.drop_table('tv')
    op.drop_table('movie_production_countries')
    op.drop_table('movie_production_companies')
    op.drop_table('movie_genre')
    op.drop_table('spoken_languages')
    op.drop_table('seasons')
    op.drop_table('production_countries')
    op.drop_table('production_companies')
    op.drop_table('networks')
    op.drop_index(op.f('ix_movies_id_movie'), table_name='movies')
    op.drop_table('movies')
    op.drop_table('last_episode_to_air')
    op.drop_table('genres')
    # ### end Alembic commands ###
