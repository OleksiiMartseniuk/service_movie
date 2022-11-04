from service_movie.base.themoviedb import schemas
from enum import Enum


class ActionTest(Enum):
    TEST_ITEM = ('item_test', 'schema_test')

    def __init__(self, action: str, schema: str) -> None:
        self.action = action
        self.schema = schema


mock_get_link_method = 'service_movie.base.themoviedb.ribbon.'\
                       'MovieApi._MovieApi__get_link_method'
mock_path_get_count_page = 'service_movie.base.themoviedb.ribbon.'\
                           'MovieApi._MovieApi__get_count_page'
mock_path_get = 'service_movie.base.themoviedb.api.TheMovieDatabaseApi.get'

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
                'overview': 'Пол Эджкомб - начальник блока смертников',
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
top_rating_movie_list_schema = schemas.TopRatingMovieList(
    data=[top_rating_movie for _ in range(top_rating_movie['total_pages'])]
)

popular_movie = {
    'page': 1,
    'results':
        [
            {
                'adult': False,
                'backdrop_path': '/y5Z0WesTjvn59jP6yo459eUsbli.jpg',
                'genre_ids': [27, 53],
                'id': 663712,
                'original_language': 'en',
                'original_title': 'Terrifier 2',
                'overview': 'Клоун-убийца Арт воскрешен по воле ',
                'popularity': 7117.087,
                'poster_path': '/uHEQd4NgQQ48q9MkhvE7ZXEfVAS.jpg',
                'release_date': '2022-11-03',
                'title': 'Ужасающий 2',
                'video': False,
                'vote_average': 7.2,
                'vote_count': 305
            },
            {
                'adult': False,
                'backdrop_path': '/tIX6j3NzadlwGcJ52nuWdmtOQkg.jpg',
                'genre_ids': [27, 53, 9648], 'id': 717728,
                'original_language': 'en',
                'original_title': 'Jeepers Creepers: Reborn',
                'overview': 'Вместе со своим парнем-гиком Лэйн оправляется',
                'popularity': 2320.615,
                'poster_path': '/yvzqzHmX9F54g4FNLM49YNup8Vi.jpg',
                'release_date': '2022-09-15',
                'title': 'Джиперс Криперс: Возрожденный',
                'video': False,
                'vote_average': 5.8,
                'vote_count': 404
            },
            {
                'adult': False,
                'backdrop_path': '/5GA3vV1aWWHTSDO5eno8V5zDo8r.jpg',
                'genre_ids': [27, 53],
                'id': 760161,
                'original_language': 'en',
                'original_title': 'Orphan: First Kill',
                'overview': '2007 год. Сбежав из эстонской психиатрическо',
                'popularity': 1964.552,
                'poster_path': '/i4BaMES0YBSAu4JYz4OFQTAgJBL.jpg',
                'release_date': '2022-08-11',
                'title': 'Дитя тьмы: первая жертва',
                'video': False,
                'vote_average': 6.8,
                'vote_count': 1195
            },
        ],
    'total_pages': 1009,
    'total_results': 20176
}

popular_movie_schema = schemas.PopularMovie(**popular_movie)
popular_movie_list_schema = schemas.PopularMovieList(
    data=[popular_movie for _ in range(500)]
)

upcoming_movie = {
    'dates': {'maximum': '2022-11-24', 'minimum': '2022-11-01'},
    'page': 1, 'results':
        [
            {
                'adult': False,
                'backdrop_path': '/y5Z0WesTjvn59jP6yo459eUsbli.jpg',
                'genre_ids': [27, 53],
                'id': 663712,
                'original_language': 'en',
                'original_title': 'Terrifier 2',
                'overview': 'Клоун-убийца Арт воскрешен по воле зловещей',
                'popularity': 7117.087,
                'poster_path': '/uHEQd4NgQQ48q9MkhvE7ZXEfVAS.jpg',
                'release_date': '2022-11-03',
                'title': 'Ужасающий 2',
                'video': False,
                'vote_average': 7.2,
                'vote_count': 305
            },
            {
                'adult': False,
                'backdrop_path': '/yYrvN5WFeGYjJnRzhY0QXuo4Isw.jpg',
                'genre_ids': [28, 12, 878],
                'id': 505642,
                'original_language': 'en',
                'original_title': 'Black Panther: Wakanda Forever',
                'overview': 'После смерти короля Т`Чаллы королева Рамонда',
                'popularity': 525.844,
                'poster_path': '/i27h6Xru52Piif1V5ZZA0ZXlck1.jpg',
                'release_date': '2022-11-10',
                'title': 'Чёрная пантера: Ваканда навеки',
                'video': False,
                'vote_average': 0,
                'vote_count': 0
            },
            {
                'adult': False,
                'backdrop_path': '/fI8hv1IqWUIUjx4YRfl6TWhdqHW.jpg',
                'genre_ids': [18, 28],
                'id': 626872,
                'original_language': 'ko',
                'original_title': '비상선언',
                'overview': 'На борту забитого до отказа авиалайнера',
                'popularity': 153.496,
                'poster_path': '/8oGFB2S8cauOFl20ry90kT5gdcd.jpg',
                'release_date': '2022-11-03',
                'title': 'Чрезвычайная ситуация',
                'video': False,
                'vote_average': 7.3,
                'vote_count': 58
            },
        ],
    'total_pages': 3,
    'total_results': 44
}

upcoming_movie_schema = schemas.UpcomingMovie(**upcoming_movie)
upcoming_movie_list_schema = schemas.UpcomingMovieList(
    data=[upcoming_movie for _ in range(upcoming_movie['total_pages'])]
)

top_rating_tv = {
    'page': 1,
    'results':
        [
            {
                'backdrop_path': '/99vBORZixICa32Pwdwj0lWcr8K.jpg',
                'first_air_date': '2021-09-03',
                'genre_ids': [10764],
                'id': 130392,
                'name': "The D'Amelio Show",
                'origin_country': ['US'],
                'original_language': 'en',
                'original_name': "The D'Amelio Show",
                'overview': '',
                'popularity': 33.099,
                'poster_path': '/phv2Jc4H8cvRzvTKb9X1uKMboTu.jpg',
                'vote_average': 9,
                'vote_count': 3117
            },
            {
                'backdrop_path': '/84XPpjGvxNyExjSuLQe0SzioErt.jpg',
                'first_air_date': '2008-01-20',
                'genre_ids': [18],
                'id': 1396,
                'name': 'Во все тяжкие',
                'origin_country': ['US'],
                'original_language': 'en',
                'original_name': 'Breaking Bad',
                'overview': 'Вся жизнь немолодого школьного учителя химии',
                'popularity': 542.675,
                'poster_path': '/3NA1FOlnjE909OyVT534B7fw5h5.jpg',
                'vote_average': 8.8,
                'vote_count': 10244
            },
            {
                'backdrop_path': '/rkB4LyZHo1NHXFEDHl9vSD9r1lI.jpg',
                'first_air_date': '2021-11-06',
                'genre_ids': [16, 10765, 10759, 18],
                'id': 94605,
                'name': 'Аркейн',
                'origin_country': ['US'],
                'original_language': 'en',
                'original_name': 'Arcane',
                'overview': 'История разворачивается в\xa0утопическом краю',
                'popularity': 98.446,
                'poster_path': '/wKve1C9FgzQlI7EsALktyplQ5NZ.jpg',
                'vote_average': 8.7,
                'vote_count': 2650
            },
        ],
    'total_pages': 133,
    'total_results': 2648
}

top_rating_tv_schema = schemas.TopRatedTV(**top_rating_tv)
top_rating_tv_list_schema = schemas.TopRatedTVList(
    data=[top_rating_tv for _ in range(top_rating_tv['total_pages'])]
)

popular_tv = {
    'page': 1,
    'results':
        [
            {
                'backdrop_path': '/etj8E2o0Bud0HkONVQPjyCkIvpv.jpg',
                'first_air_date': '2022-08-21',
                'genre_ids': [10765, 18, 10759],
                'id': 94997,
                'name': 'Дом Дракона',
                'origin_country': ['US'],
                'original_language': 'en',
                'original_name': 'House of the Dragon',
                'overview': 'Члены дома Таргариенов оставляют обречённую',
                'popularity': 4034.906,
                'poster_path': '/emAFaKrAn1mhJ3ZQbM2503a1X2s.jpg',
                'vote_average': 8.5,
                'vote_count': 2231
            },
            {
                'backdrop_path': '/i9htchhoOl26cLaslVHXHghgLt0.jpg',
                'first_air_date': '2015-10-19',
                'genre_ids': [10759, 16, 10762],
                'id': 65334,
                'name': 'Леди Баг и Супер-кот',
                'origin_country': ['FR'],
                'original_language': 'fr',
                'original_name': 'Miraculous, les aventures de Ladybug',
                'overview': 'Адриан и\xa0Маринетт\xa0— старшеклассники, почти',
                'popularity': 2592.78,
                'poster_path': '/yc7WYrxhw7PdeTGrrq2pvTWkgaO.jpg',
                'vote_average': 8,
                'vote_count': 3840
            },
            {
                'backdrop_path': '/1rO4xoCo4Z5WubK0OwdVll3DPYo.jpg',
                'first_air_date': '2022-09-01',
                'genre_ids': [10765, 10759, 18],
                'id': 84773,
                'name': 'Властелин колец: Кольца власти',
                'origin_country': ['US'],
                'original_language': 'en',
                'original_name': 'The Lord of the Rings: The Rings of Power',
                'overview': 'Несмотря на\xa0то, что\xa0наступили времена',
                'popularity': 2374.417,
                'poster_path': '/gGX72S7AY4ZvdK8bCZ6ga2SAnY.jpg',
                'vote_average': 7.6,
                'vote_count': 1391
            },
        ],
    'total_pages': 6967,
    'total_results': 139323
}

popular_tv_schema = schemas.PopularTV(**popular_tv)
popular_tv_list_schema = schemas.PopularTVList(
    data=[popular_tv for _ in range(500)]
)

languages = [
    {
        'iso_3166_1': 'AD',
        'english_name': 'Andorra',
        'native_name': 'Andorra'
    },
    {
        'iso_3166_1': 'AE',
        'english_name': 'United Arab Emirates',
        'native_name': 'United Arab Emirates'
    },
    {
        'iso_3166_1': 'AF',
        'english_name': 'Afghanistan',
        'native_name': 'Afghanistan'
    }
]

countries = [
    {
        'iso_3166_1': 'ZM',
        'english_name': 'Zambia',
        'native_name': 'Zambia'
    },
    {
        'iso_3166_1': 'ZR',
        'english_name': 'Zaire',
        'native_name': 'Zaire'
    },
    {
        'iso_3166_1': 'ZW',
        'english_name': 'Zimbabwe',
        'native_name': 'Zimbabwe'
    }
]
