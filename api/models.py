"""SQLAlchemy Database models."""

import sqlalchemy as sa
from db import db

class Book(db.Model):
    """Represents a biblographic record for a book."""
    id        = sa.Column(sa.Integer, primary_key=True)
    title     = sa.Column(sa.String, nullable=False)
    author    = sa.Column(sa.String)
    text_url  = sa.Column(sa.String, nullable=False)
    cover_url = sa.Column(sa.String)
