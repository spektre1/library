"""Using the gutenberg100.json, load into db through API."""

import requests
import json
from db import db
from models import Book, Author

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
    b = Book(**{k: book[k] for k in props})
    b.author.append(Author(name=book['author']))
    db.session.add(b)
    db.session.commit()