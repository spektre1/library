"""Operations to modify bibliographic metadata (books) in the database."""
from flask import request
from models import Author, Book
from db import db

props = [
    'title',
    'text_url',
    'cover_url'
]

def add():
    """Adds a book to the library db."""
    j = request.json
    book = Book(**{p: j[p] for p in props})
    book.author.append(Author(name=j['author']))
    db.session.add(book)
    db.session.commit()
    return f"Successfully uploaded #{book.id} - {j['title']}"


def get(id:int):
    """Gets a bibliographic metadata by id."""
    book = Book.query.get(id)
    return {prop:getattr(book, prop) for prop in props}
