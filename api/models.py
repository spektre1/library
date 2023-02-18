import sqlalchemy as sa
from db import db

class Book(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    author = sa.Column(sa.String)
    copyright = sa.Column(sa.String)

class Gutenberg(db.Model):
    id = sa.Column(sa.Integer, primary_key=True) #ebook_no.
    bookID = sa.Column(sa.Integer, sa.ForeignKey(Book.id))
    coverURL = sa.Column(sa.String)
    textURL = sa.Column(sa.String)
