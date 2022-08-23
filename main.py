from os import abort
from flask import Flask, request
import json
import sqlite3

from utils import get_film_by_title

app = Flask(__name__)


@app.get('/movie/<title>')
def search_title(title):
    """
    Выдает фильм по назваонию
    """
    if title is None:
        abort(404)

    result = get_film_by_title(title)

    if result != dict:
        return result

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
