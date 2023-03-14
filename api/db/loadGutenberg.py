"""Using the gutenberg100.json, load into db through API."""

import requests
import json
from models import Book, Author, db_session

props = ['title', 'text_url', 'cover_url']

with open('gutenberg100.json', 'r') as f:
    books = json.load(f)

# for book in books:
#     resp = requests.post(
#         url='http://localhost:5000/api/v1/book/add',
#         json={prop:book[prop] for prop in props})
#     if resp.status_code !=200:
#         print(f'oh noes! Resp status {resp.status}: {resp.body}')
# 



for book in books:
    # skip books we've already added by title:
    if Book.query.filter_by(title=book['title']).scalar():
        continue
    b = Book(**{k: book[k] for k in props})
    if isinstance(book['author'], list):
        for a in book['author']:
            existantAuthor = Author.query.filter_by(name=a).scalar()
            if existantAuthor:
                b.author.append(existantAuthor)
            else:
                b.author.append(Author(name=a))
    else:
        existantAuthor = Author.query.filter_by(name=book['author']).scalar()
        if existantAuthor:
            b.author.append(existantAuthor)
        else:
            b.author.append(Author(name=book['author']))
    db_session.add(b)
    db_session.commit()


db_session.rollback()