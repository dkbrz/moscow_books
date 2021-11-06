from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import types
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import json

db = SQLAlchemy()


class Books(db.Model):
    __tablename__ = "books"

    id = db.Column("id", db.Integer, index=True, primary_key=True)
    title = db.Column("title", db.Text)
    author = db.Column("author", db.Text)


class Recommendation(db.Model):
    __tablename__ = "recommendations"
    iduser = db.Column("iduser", db.Integer, index=True, primary_key=True)
    idbook = db.Column("book", db.Integer, ForeignKey("books.id"), index=True, primary_key=True)
    book = relationship("Books", lazy='joined')


class History(db.Model):
    __tablename__ = "history"
    iduser = db.Column("iduser", db.Integer, index=True, primary_key=True)
    idbook = db.Column("book", db.Integer, ForeignKey("books.id"), index=True, primary_key=True)
    book = relationship("Books", lazy='joined')
