from service_movie.base.themoviedb import schemas


genres = {
    'genres':
        [
            {'id': 28, 'name': 'боевик'},
            {'id': 12, 'name': 'приключения'},
            {'id': 16, 'name': 'мультфильм'}
        ]
    }


genres_schema = schemas.Genres(**genres)
