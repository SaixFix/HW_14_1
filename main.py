from os import abort
from flask import Flask, request
import json
import sqlite3

from utils import get_film_by_title, get_film_by_select_years, get_film_by_rating, get_film_by_genre

app = Flask(__name__)


@app.route('/movie/<title>')
def search_title(title):
    """
    Выдает фильм по назваонию
    """
    if title is None:
        abort(404)

    result = get_film_by_title(title)

    return result


@app.route('/movie/year/to/year')
def search_movie_by_years():
    """
    Выдает список фильмов по указанному диапозону лет
    """
    a = request.args['a']
    b = request.args['b']
    result = get_film_by_select_years(a, b)

    return result


@app.route('/rating/children')
def movie_by_rating_children():
    """
    Список фильмов с рейтингом children: G
    """
    return get_film_by_rating('("G")')


@app.route('/rating/family')
def movie_by_rating_family():
    """
    Список фильмов с рейтингом family: "G", "PG", "PG-13"
    """
    rating = ("G", "PG", "PG-13")
    return get_film_by_rating(rating)


@app.route('/rating/adult')
def movie_by_rating_adult():
    """
    Список фильмов с рейтингом adult: "R", "NC-17"
    """
    rating = ("R", "NC-17")
    return get_film_by_rating(rating)


@app.route('/genre/<genre>')
def movie_by_genre(genre):
    """
    Принимает жанр, возвращает список фильмов по жару с
    """
    return get_film_by_genre(genre)




@app.errorhandler(404)
def not_found_error(error):
    """
    вьюшка возвращает текст при ошибке 404
    """
    return "404! Страница не найдена! Истина где-то рядом..."


@app.errorhandler(500)
def not_found_error(error):
    """
    вьюшка возвращает текст при ошибке 500
    """
    return "500! Чтото пошло не так"


if __name__ == "__main__":
    app.run()
