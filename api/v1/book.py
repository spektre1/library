"""Operations to modify bibliographic metadata (books) in the database."""
from flask import request
from models import Book
from db import db

props = [
    'title',
    'author',
    'text_url',
    'cover_url'
]

def add():
    """Adds a book to the library db."""
    j = request.json
    book = Book(
        title=j['Title'],
        author=j['Author'],
        text_url=j['textURL'],
        cover_url=j['coverImgURL']
    )
    db.session.add(book)
    db.session.commit()
    return f"Successfully uploaded #{book.id} - {j['Title']}"


def get(id:int):
    """Gets a bibliographic metadata by id."""
    book = Book.query.get(id)
    return {prop:getattr(book, prop) for prop in props}
