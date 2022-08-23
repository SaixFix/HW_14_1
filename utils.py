import sqlite3
import json


def connection_sql_base(query, uid):
    """
     Читаем из базы netflix.db по запросу
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        return cursor.execute(query, uid)


def get_film_by_title(title) -> dict or None:
    """
    возвращает информацию о фильме по названию
    """
    query = """
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title = (?)
                    ORDER BY release_year
                """
    item = connection_sql_base(query, (title,))
    item_1 = item.fetchone()

    if item_1 is None:
        return "Такого фильма не найдено"

    film_info = {
        "title": item_1[0],
        "country": item_1[1],
        "release_year": item_1[2],
        "genre": item_1[3],
        "description": item_1[4]
    }
    return json.dumps(film_info)


def get_film_by_select_years(from_years, to_years):
    """
    Делает выборгу фильмоb по годам выпуска, принимая 2 значения от и до
    """

    query = """
                        SELECT title, release_year
                        FROM netflix
                        WHERE release_year BETWEEN (?) AND (?)
                        ORDER BY release_year
                        LIMIT 100
                    """
    item = connection_sql_base(query, (from_years, to_years))
    item_1 = item.fetchall()

    if item_1 is None:
        return "Такого фильма не найдено"

    list_film = []
    for i in item_1:
        films = {
            "title": i[0],
            "release_year": i[1],
        }
        list_film.append(films)

    return json.dumps(list_film)


#
# lol  = get_film_by_select_yers(1945, 1960)
# # for i in lol:
# print(lol)
