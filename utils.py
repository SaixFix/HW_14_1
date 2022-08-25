import sqlite3
import json


def connection_sql_base(query):
    """
     Читаем из базы netflix.db по запросу
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        return cursor.execute(query).fetchall()


def get_film_by_title(title) -> dict or None:
    """
    возвращает информацию о фильме по названию
    """
    query = f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title = {title}
                    ORDER BY release_year DESC
                """
    item = connection_sql_base(query)

    if item is None:
        return "Такого фильма не найдено"

    film_info = {
        "title": item[0][0],
        "country": item[0][1],
        "release_year": item[0][2],
        "genre": item[0][3],
        "description": item[0][4]
    }
    return json.dumps(film_info)


def get_film_by_select_years(from_years, to_years):
    """
    Делает выборrу фильмоb по годам выпуска, принимая 2 значения от и до
    """

    query = f"""
                        SELECT title, release_year
                        FROM netflix
                        WHERE release_year BETWEEN {from_years} AND {to_years}
                        ORDER BY release_year
                        LIMIT 100
                    """
    item = connection_sql_base(query)

    if item is None:
        return "Такого фильма не найдено"

    list_film = []
    for i in item:
        films = {
            "title": i[0],
            "release_year": i[1],
        }
        list_film.append(films)

    return json.dumps(list_film)


def get_film_by_rating(rating):
    """
    Делает выборrу фильмов по заданному возрастному рейтингу
    """
    query = f"""
                        SELECT title, rating, description 
                        FROM netflix
                        WHERE rating in {rating}
                        ORDER BY release_year
                    """
    item = connection_sql_base(query)

    list_film = []
    for i in item:
        films = {
            "title": i[0],
            "rating": i[1],
            "release_year": i[2]
        }
        list_film.append(films)

    return json.dumps(list_film)


#
# lol  = get_film_by_select_yers(1945, 1960)
# # for i in lol:
print(get_film_by_rating('("G")'))
