from os import abort
from flask import Flask, request
import json
import sqlite3

from utils import get_film_by_title, get_film_by_select_years

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

    # if a != int or a == '':
    #     abort(404)
    # elif b != int or b == '':
    #     abort(404)

    return result


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
