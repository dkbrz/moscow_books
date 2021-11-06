import sqlalchemy as _sql
import bookapp.database as _database


class Books(_database.Base):
    __tablename__ = "books"

    id = _sql.Column("id", _sql.Integer, index=True, primary_key=True)
    title = _sql.Column("title", _sql.Text)
    author = _sql.Column("author", _sql.Text)


class Recommendation(_database.Base):
    __tablename__ = "recommendations"
    iduser = _sql.Column("iduser", _sql.Integer, index=True, primary_key=True)
    idbook = _sql.Column("book", _sql.Integer, _sql.ForeignKey("books.id"), index=True, primary_key=True)
    book = _sql.orm.relationship("Books", lazy='joined')


class History(_database.Base):
    __tablename__ = "history"
    iduser = _sql.Column("iduser", _sql.Integer, index=True, primary_key=True)
    idbook = _sql.Column("book", _sql.Integer, _sql.ForeignKey("books.id"), index=True, primary_key=True)
    book = _sql.orm.relationship("Books", lazy='joined')
