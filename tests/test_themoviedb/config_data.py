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

movie = {
    'adult': False,
    'backdrop_path': None,
    'belongs_to_collection': None,
    'budget': 0,
    'genres': [],
    'homepage': '',
    'id': 72925,
    'imdb_id': 'tt0334998',
    'original_language': 'en',
    'original_title': 'Chris Botti & Friends - Night Sessions:',
    'overview': '',
    'popularity': 1.704,
    'poster_path': '/eRUO6x7RLPtaoz3YEWIDc8We135.jpg',
    'production_companies': [],
    'production_countries': [],
    'release_date': '2002-08-06',
    'revenue': 0,
    'runtime': 85,
    'spoken_languages': [],
    'status': 'Released',
    'tagline': '',
    'title': 'Chris Botti & Friends - Night Sessions: Live in Concert',
    'video': False,
    'vote_average': 6.9,
    'vote_count': 16
}

movie_schema = schemas.Movie(**movie)

tv = {
    'adult': False,
    'backdrop_path': '/qT9O4Qfcc5v2YAgFmcuCow02Aai.jpg',
    'created_by':
        [
            {
                'id': 77897,
                'credit_id': '52534f6519c295794011063e',
                'name': 'Tyra Banks',
                'gender': 1,
                'profile_path': '/g5Aar3pS2imJowLgk0GVawyggvf.jpg'
            }
        ],
    'episode_run_time': [42],
    'first_air_date': '2003-05-20',
    'genres': [{'id': 10764, 'name': 'Реалити-шоу'}],
    'homepage': 'http://www.vh1.com/shows/americas-next-top-model',
    'id': 331,
    'in_production': True,
    'languages': ['en'],
    'last_air_date': '2018-04-10',
    'last_episode_to_air':
        {
            'air_date': '2018-04-10',
            'episode_number': 14,
            'id': 1469155,
            'name': 'Эпизод 14',
            'overview': '',
            'production_code': '',
            'runtime': 42,
            'season_number': 24,
            'show_id': 331,
            'still_path': None,
            'vote_average': 0.0,
            'vote_count': 0
        },
    'name': 'Топ-модель по-американски',
    'next_episode_to_air': None,
    'networks':
        [
            {
                'id': 40,
                'name': 'UPN',
                'logo_path': '/333LtWX9Z7H9uRrNcCl1JcTvdpR.png',
                'origin_country': 'US'
            },
            {
                'id': 71,
                'name': 'The CW',
                'logo_path': '/ge9hzeaU7nMtQ4PjkFlc68dGAJ9.png',
                'origin_country': 'US'
            },
            {
                'id': 158,
                'name': 'VH1',
                'logo_path': '/w9oUxxUiXTC1O1MzJSvsMjQbgft.png',
                'origin_country': 'US'
            }
        ],
    'number_of_episodes': 311,
    'number_of_seasons': 24,
    'origin_country': ['US'],
    'original_language': 'en',
    'original_name': "America's Next Top Model",
    'overview': 'Ведущая и организатор шоу супермодель Тайра Бэнкс ',
    'popularity': 40.35,
    'poster_path': '/47EIfjYrT80AOfpAIkvSxdpwGOv.jpg',
    'production_companies':
        [
            {
                'id': 58907,
                'logo_path': None,
                'name': '10 by 10 Entertainment',
                'origin_country': ''
            },
            {
                'id': 58908,
                'logo_path': None,
                'name': 'Bankable Productions',
                'origin_country': 'US'
            }
        ],
    'production_countries':
        [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
    'seasons':
        [
            {
                'air_date': '2008-02-06',
                'episode_count': 12,
                'id': 62681,
                'name': 'Спецматериалы',
                'overview': '',
                'poster_path': None,
                'season_number': 0
            },
            {
                'air_date': '2003-05-20',
                'episode_count': 8,
                'id': 62679,
                'name': 'Сезон 1',
                'overview': '',
                'poster_path': '/wzXNJigswbWjtz9JskBoOX0Dze4.jpg',
                'season_number': 1
            },
            {
                'air_date': '2004-01-13',
                'episode_count': 10,
                'id': 62680,
                'name': 'Сезон 2',
                'overview': '',
                'poster_path': '/vowlMza06g3MC2xD2EWGvr07uyL.jpg',
                'season_number': 2
            },
            {
                'air_date': '2004-09-22',
                'episode_count': 13,
                'id': 62682,
                'name': 'Сезон 3',
                'overview': '',
                'poster_path': '/8jFQW2c8Rse95ZbOLr5Ch6iZPuy.jpg',
                'season_number': 3
            },
            {
                'air_date': '2005-03-02',
                'episode_count': 12,
                'id': 62683,
                'name': 'Сезон 4',
                'overview': '',
                'poster_path': '/nXKhb9BkKltzdHtCliST9Mbp3MT.jpg',
                'season_number': 4
            },
            {
                'air_date': '2005-09-21',
                'episode_count': 12,
                'id': 62684,
                'name': 'Сезон 5',
                'overview': '',
                'poster_path': '/5Fp9gd5WuY2z3PsM2aRRiKagey1.jpg',
                'season_number': 5
            },
            {
                'air_date': '2006-03-08',
                'episode_count': 12,
                'id': 62685,
                'name': 'Сезон 6',
                'overview': '',
                'poster_path': '/tPGbziZtnuUhI4sbIcngYZHvTTa.jpg',
                'season_number': 6
            },
            {
                'air_date': '2006-09-20',
                'episode_count': 13,
                'id': 62686,
                'name': 'Сезон 7',
                'overview': '',
                'poster_path': '/uPvTVYG7La3g4xRySiCWTfGuM9j.jpg',
                'season_number': 7
            },
            {
                'air_date': '2007-02-28',
                'episode_count': 13,
                'id': 62687,
                'name': 'Сезон 8',
                'overview': '',
                'poster_path': '/gWZgy15H1vCri1c2dqjPBpslhTU.jpg',
                'season_number': 8
            },
        ],
    'spoken_languages':
        [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}],
    'status': 'Returning Series',
    'tagline': '',
    'type': 'Reality',
    'vote_average': 5.336,
    'vote_count': 110
}

tv_schema = schemas.TV(**tv)

top_rating_movie = {
    'page': 1,
    'results':
        [
            {
                'adult': False,
                'backdrop_path': '/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg',
                'genre_ids': [18, 80],
                'id': 278,
                'original_language': 'en',
                'original_title': 'The Shawshank Redemption',
                'overview': 'Фильм удостоен шести номинаций на\xa0«Оскар»,',
                'popularity': 93.513,
                'poster_path': '/yvmKPlTIi0xdcFQIFcQKQJcI63W.jpg',
                'release_date': '2019-10-24',
                'title': 'Побег из Шоушенка',
                'video': False,
                'vote_average': 8.7,
                'vote_count': 22576
            },
            {
                'adult': False,
                'backdrop_path': '/zb6fM1CX41D9rF9hdgclu0peUmy.jpg',
                'genre_ids': [18, 36, 10752],
                'id': 424,
                'original_language': 'en',
                'original_title': "Schindler's List",
                'overview': 'Лента рассказывает реальную историю ',
                'popularity': 63.97,
                'poster_path': '/4K8fGGcJP2EoGDucILnaJcOJhZl.jpg',
                'release_date': '1994-05-21',
                'title': 'Список Шиндлера',
                'video': False,
                'vote_average': 8.6,
                'vote_count': 13400
            },
            {
                'adult': False,
                'backdrop_path': '/Ab8mkHmkYADjU7wQiOkia9BzGvS.jpg',
                'genre_ids': [16, 10751, 14],
                'id': 129,
                'original_language': 'ja',
                'original_title': '千と千尋の神隠し',
                'overview': 'Маленькая Тихиро вместе с мамой и папой',
                'popularity': 97.61,
                'poster_path': '/rq2IzPgweryLrN3H19Jjh1TtBxf.jpg',
                'release_date': '2002-12-31',
                'title': 'Унесённые призраками',
                'video': False,
                'vote_average': 8.5,
                'vote_count': 13495
            },
            {
                'adult': False,
                'backdrop_path': '/mMtUybQ6hL24FXo0F3Z4j2KG7kZ.jpg',
                'genre_ids': [10749, 16, 18],
                'id': 372058,
                'original_language': 'ja',
                'original_title': '君の名は。',
                'overview': 'Токийский парень Таки и провинциальная девушка',
                'popularity': 148.805,
                'poster_path': '/iUQlwEFo90cUHD3MINhbhz3V8cR.jpg',
                'release_date': '2018-01-03',
                'title': 'Твоё имя',
                'video': False,
                'vote_average': 8.5,
                'vote_count': 9190
            },
            {
                'adult': False,
                'backdrop_path': '/TU9NIjwzjoKPwQHoHshkFcQUCG.jpg',
                'genre_ids': [35, 53, 18],
                'id': 496243,
                'original_language': 'ko',
                'original_title': '기생충',
                'overview': 'Обычное корейское семейство жизнь не балует',
                'popularity': 71.389,
                'poster_path': '/zg3lUyLTnpbS5N29G6B3a63O7uP.jpg',
                'release_date': '2019-07-04',
                'title': 'Паразиты',
                'video': False,
                'vote_average': 8.5,
                'vote_count': 14635
            },
            {
                'adult': False,
                'backdrop_path': '/l6hQWH9eDksNJNiXWYRkWqikOdu.jpg',
                'genre_ids': [14, 18, 80],
                'id': 497,
                'original_language': 'en',
                'original_title': 'The Green Mile',
                'overview': 'Пол Эджкомб - начальник блока смертников в тюрьме',
                'popularity': 76.954,
                'poster_path': '/qm54bHOkvwnrSvLHdHnhdmi7PUy.jpg',
                'release_date': '2000-04-18',
                'title': 'Зелёная миля',
                'video': False,
                'vote_average': 8.5,
                'vote_count': 14563
            },
            {
                'adult': False,
                'backdrop_path': '/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg',
                'genre_ids': [18, 28, 80, 53],
                'id': 155,
                'original_language': 'en',
                'original_title': 'The Dark Knight',
                'overview': 'Бэтмен поднимает ставки в войне с криминалом.',
                'popularity': 98.045,
                'poster_path': '/dxWaYQtgpLbycqUpHzkqqYkT5I3.jpg',
                'release_date': '2008-08-14',
                'title': 'Тёмный рыцарь',
                'video': False,
                'vote_average': 8.5,
                'vote_count': 28508
            },
        ],
        'total_pages': 142,
        'total_results': 282
}

top_rating_movie_schema = schemas.TopRatingMovie(**top_rating_movie)
