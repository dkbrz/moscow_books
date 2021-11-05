from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import types
import zlib
import json
from demoapp.default_recommendation import DEFAULT_RECOMMENDATION

db = SQLAlchemy()


class CompressedJSON(types.TypeDecorator):
    impl = types.LargeBinary

    def process_result_value(self, value, dialect):
        if value is None:
            return []
        res = json.loads(zlib.decompress(value).decode("utf-8"))
        return res


class Recommendation(db.Model):
    __tablename__ = "recommendations"
    id = db.Column("id", db.Integer, primary_key=True, index=True)
    history = db.Column(CompressedJSON)
    recommendations = db.Column(CompressedJSON, default=DEFAULT_RECOMMENDATION)
