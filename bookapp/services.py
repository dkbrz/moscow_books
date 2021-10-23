import sqlalchemy.orm as _orm

import bookapp.database as _database
from bookapp.models import (
    Recommendations,
    DEFAULT_RECOMMENDATION,
    RecommendationsShort,
)


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.async_session()
    try:
        yield db
    finally:
        db.close()


async def get_basic(userid: int, db: _orm.Session):
    result = await db.get(Recommendations, userid)
    if result is None:
        result = Recommendations(id=0, history=[], recommendations=DEFAULT_RECOMMENDATION)
    return result


async def get_short(userid: int, db: _orm.Session):
    result = await db.get(RecommendationsShort, userid)
    if result is None:
        result = RecommendationsShort(id=0, history=[], recommendations=DEFAULT_RECOMMENDATION)
    return result
