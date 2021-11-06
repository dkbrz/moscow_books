import sqlalchemy.orm as _orm
from sqlalchemy import select

import bookapp.database as _database
from bookapp.models import (
    Recommendation,
    History
)


class Result:

    def __init__(self, uid, history, recommend):
        self.id = uid
        self.add("history", history)
        self.add("recommendations", recommend)

    def add(self, attr, value_list):
        setattr(self, attr, [
            {"id": b[0].book.id, "title": b[0].book.title, "author": b[0].book.author}
            for b in value_list
        ])


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.async_session()
    try:
        yield db
    finally:
        db.close()


async def get_basic(userid: int, db: _orm.Session):
    recommend = await db.execute(select(Recommendation).filter(Recommendation.iduser == userid))
    history = await db.execute(select(History).filter(History.iduser == userid))
    result = Result(userid, history, recommend)
    if not result.recommendations:
        recommend = await db.execute(select(Recommendation).filter(Recommendation.iduser == 0))
        result.add("recommendations", recommend)
    return result
