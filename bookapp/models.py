import sqlalchemy as _sql
import bookapp.database as _database
from bookapp.default_recommendation import DEFAULT_RECOMMENDATION


class Recommendations(_database.Base):
    __tablename__ = "recommendations"
    id = _sql.Column("id", _sql.Integer, primary_key=True, index=True)
    history = _sql.Column(_sql.JSON)
    recommendations = _sql.Column(_sql.JSON, default=DEFAULT_RECOMMENDATION)


class RecommendationsShort(_database.Base):
    __tablename__ = "recommendations_short"
    id = _sql.Column("id", _sql.Integer, primary_key=True, index=True)
    history = _sql.Column(_sql.JSON)
    recommendations = _sql.Column(_sql.JSON, default=DEFAULT_RECOMMENDATION)
