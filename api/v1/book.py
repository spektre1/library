"""Operations to modify books in the database."""
from flask import request


def add():
    """Adds a book to the library db."""
    print("Add called, JSON is: ", request.json)

