"""Operations to modify books in the database."""
from flask import request


def add():
    """Adds a book to the library db."""
    j = request.json
    print(j)
    return f"Successfully uploaded{j['Title']}"

