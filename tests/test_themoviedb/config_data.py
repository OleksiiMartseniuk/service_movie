from service_movie.base.themoviedb import schemas

params_default = {'api_key': 'test_token', 'language': 'ru-Ru'}
params_data = {'params1': 'params1', 'params2': None}
params_result = {
    'api_key': 'test_token',
    'language': 'ru-Ru',
    'params1': 'params1'
}

genres = {
    'genres':
        [
            {'id': 28, 'name': 'боевик'},
            {'id': 12, 'name': 'приключения'},
            {'id': 16, 'name': 'мультфильм'}
        ]
    }


genres_schema = schemas.Genres(**genres)
