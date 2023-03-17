"""Using the gutenberg100.json, load into db through API."""

import requests
import json
from models import Book, Author, db_session

props = ['title', 'text_url', 'cover_url']

with open('gutenberg100.json', 'r') as f:
    books = json.load(f)


for book in books:
    # skip books we've already added by title:
    if Book.query.filter_by(title=book['title']).scalar():
        continue
    b = Book(**{k: book[k] for k in props})
    for a in book['author']:
        author = Author.query.filter_by(name=a).scalar()
        if not author:
            author = Author(name=a)
        b.author.append(author)
    db_session.add(b)
    db_session.commit()

# db_session.rollback()
