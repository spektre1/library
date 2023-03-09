"""SQLAlchemy Database models."""

import sqlalchemy as sa
from sqlalchemy import Integer, String, ForeignKey, Column, Table
from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from db import db

class Base(DeclarativeBase):
    pass

# Represents the relationship of authors to a book.
book_authors = Table(
    'book_authors',
    Base.metadata,
    Column('author_id', ForeignKey('authors.id')),
    Column('book_id', ForeignKey('books.id'))
    )


class Author(Base):
    """Represents an author."""
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Book(Base):
    """Represents a book."""
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[List["Author"]] = relationship('Author', secondary=book_authors, backref='books')
    text_url: Mapped[str]
    cover_url: Mapped[Optional[str]]
