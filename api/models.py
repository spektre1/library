"""SQLAlchemy Database models."""

from sqlalchemy import ForeignKey, Column, Table
from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///library.sqlite", echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False,
        autoflush=False,
        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
Base.session = db_session

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
    name: Mapped[str] = mapped_column(unique=True)


class Book(Base):
    """Represents a book."""
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[List["Author"]] = relationship('Author', secondary=book_authors, backref='books')
    text_url: Mapped[str]
    cover_url: Mapped[Optional[str]]


Base.metadata.create_all(bind=engine)
